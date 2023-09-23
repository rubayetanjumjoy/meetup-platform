from django.db import models
import requests
from decouple import config
from django.utils import timezone  # Import timezone
from django.core.exceptions import ValidationError  # Import ValidationError


class Venue(models.Model):
    """
    Venue model
    """

    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    def clean(self):
        # Validate latitude and longitude values
        if not (-90 <= self.latitude <= 90) or not (-180 <= self.longitude <= 180):
            raise ValidationError("Latitude and longitude values are out of range.")

    def save(self, *args, **kwargs):
        if not self.id:
            # Create a new venue
            self.create_venue()
        else:
            # Update an existing venue
            self.update_venue()

        super(Venue, self).save(*args, **kwargs)

    def create_venue(self):
        # Make API request to Eventbrite for creating
        organization_id = config("ORGANIZATION_ID")
        secret_key = config("SECRET_KEY")
        base_url = config("BASE_URL")

        headers = {
            "Authorization": f"Bearer {secret_key}",
        }

        venue_data = {
            "venue": {
                "name": self.name,
                "address": {
                    "latitude": str(self.latitude),
                    "longitude": str(self.longitude),
                },
            }
        }

        create_venue_url = f"{base_url}organizations/{organization_id}/venues/"
        response = requests.post(create_venue_url, headers=headers, json=venue_data)
        print(response.json())

        if response.status_code == 200:
            venue_info = response.json()
            self.id = venue_info["id"]
            self.name = venue_info["name"]
            self.latitude = float(venue_info["address"]["latitude"])
            self.longitude = float(venue_info["address"]["longitude"])
            print("Venue created successfully")
        else:
            # Handle any error or provide appropriate feedback
            raise ValidationError("Failed to create venue on Eventbrite")

    def update_venue(self):
        # Make API request to Eventbrite for updating
        organization_id = config("ORGANIZATION_ID")
        secret_key = config("SECRET_KEY")
        base_url = config("BASE_URL")

        headers = {
            "Authorization": f"Bearer {secret_key}",
        }

        venue_data = {
            "venue": {
                "name": self.name,
                "address": {
                    "latitude": str(self.latitude),
                    "longitude": str(self.longitude),
                },
            }
        }

        update_venue_url = f"{base_url}venues/{self.id}/"
        response = requests.post(update_venue_url, headers=headers, json=venue_data)
        print(response.json())

        if response.status_code == 200:
            venue_info = response.json()

            print("Venue updated successfully")
        else:
            # Handle any error or provide appropriate feedback
            raise ValidationError("Failed to update venue on Eventbrite")


class Event(models.Model):
    """
    Event model
    """

    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    event_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.event_link

    def clean(self):
        # Check if start_date is in the future
        if self.start_date <= timezone.now():
            raise ValidationError("Start date must be in the future.")

        # Check if start_date is earlier than end_date
        if self.start_date >= self.end_date:
            raise ValidationError("Start date must be earlier than end date.")

    # Make API request to Eventbrite
    def save(self, *args, **kwargs):
        if not self.id:
            # Create a new event
            self.create_event()
        else:
            # Update an existing event
            self.update_event()

        super(Event, self).save(*args, **kwargs)

    def create_event(self):
        # Make API request to Eventbrite for creating
        organization_id = config("ORGANIZATION_ID")
        secret_key = config("SECRET_KEY")
        base_url = config("BASE_URL")

        headers = {
            "Authorization": f"Bearer {secret_key}",
        }

        event_data = {
            "event.name.html": self.name,
            "event.start.timezone": str(timezone.get_current_timezone()),
            "event.start.utc": self.start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event.end.timezone": str(timezone.get_current_timezone()),
            "event.end.utc": self.end_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event.currency": "USD",
            "event.venue_id": self.venue_id,
        }

        create_event_url = f"{base_url}organizations/{organization_id}/events/"
        response = requests.post(create_event_url, headers=headers, json=event_data)
        print(response.json())

        if response.status_code == 200:
            event_info = response.json()
            # Update the event_link field with the Eventbrite URL
            self.event_link = event_info["url"]
            self.id = event_info["id"]
            print("Event created successfully")
        else:
            # Handle any error or provide appropriate feedback
            raise ValidationError("Failed to create event on Eventbrite")

    def update_event(self):
        # Make API request to Eventbrite for updating
        organization_id = config("ORGANIZATION_ID")
        secret_key = config("SECRET_KEY")
        base_url = config("BASE_URL")

        headers = {
            "Authorization": f"Bearer {secret_key}",
        }

        event_data = {
            "event.name.html": self.name,
            "event.start.timezone": str(timezone.get_current_timezone()),
            "event.start.utc": self.start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event.end.timezone": str(timezone.get_current_timezone()),
            "event.end.utc": self.end_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event.currency": "USD",
            "event.venue_id": self.venue_id,
        }

        update_event_url = f"{base_url}events/{self.id}/"
        response = requests.post(update_event_url, headers=headers, json=event_data)
        print(response.json())
        if response.status_code == 200:
            event_info = response.json()
            # Update any necessary fields if needed
            print("Event updated successfully")
        else:
            # Handle any error or provide appropriate feedback
            raise ValidationError("Failed to update event on Eventbrite")

    def delete(self, *args, **kwargs):
        eventbrite_event_id = self.id  # Assuming 'id' is the Eventbrite event ID
        print(eventbrite_event_id)
        # Make API request to Eventbrite to delete the event
        organization_id = config("ORGANIZATION_ID")
        secret_key = config("SECRET_KEY")
        base_url = config("BASE_URL")

        headers = {
            "Authorization": f"Bearer {secret_key}",
        }

        delete_event_url = f"{base_url}events/{eventbrite_event_id}/"
        response = requests.delete(delete_event_url, headers=headers)

        if response.status_code == 200:
            # Event deleted successfully on Eventbrite
            super(Event, self).delete(
                *args, **kwargs
            )  # Call the original delete method
        else:
            # Handle any error or provide appropriate feedback
            raise ValidationError("Failed to delete event on Eventbrite")

            
