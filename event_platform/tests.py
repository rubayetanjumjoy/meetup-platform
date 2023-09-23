from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Venue, Event
from django.utils import timezone


class VenueTestCase(TestCase):
    def test_create_venue(self):
        venue = Venue(name="Test Venue", latitude=40.7128, longitude=-74.0060)
        venue.save()
        self.assertIsNotNone(venue.id)
        self.assertEqual(venue.name, "Test Venue")

    def test_update_venue(self):
        venue = Venue(name="Test Venue", latitude=40.7128, longitude=-74.0060)
        venue.save()
        venue.name = "Updated Venue"
        venue.save()
        updated_venue = Venue.objects.get(pk=venue.id)
        self.assertEqual(updated_venue.name, "Updated Venue")

    def test_invalid_coordinates(self):
        with self.assertRaises(ValidationError):
            venue = Venue(name="Invalid Venue", latitude=1000, longitude=-2000)
            venue.full_clean()


class EventTestCase(TestCase):
    def setUp(self):
        venue = Venue.objects.create(
            name="Test Venue", latitude=40.7128, longitude=-74.0060
        )
        self.event = Event(
            name="Test Event",
            venue=venue,
            start_date=timezone.now() + timezone.timedelta(days=1),
            end_date=timezone.now() + timezone.timedelta(days=2),
            ticket_price=100.00,
        )

    def test_create_event(self):
        self.event.save()
        self.assertIsNotNone(self.event.id)
        self.assertEqual(self.event.name, "Test Event")

    def test_update_event(self):
        self.event.save()
        self.event.name = "Updated Event"
        self.event.save()
        updated_event = Event.objects.get(pk=self.event.id)
        self.assertEqual(updated_event.name, "Updated Event")

    def test_invalid_start_date(self):
        self.event.start_date = timezone.now() - timezone.timedelta(days=1)
        with self.assertRaises(ValidationError):
            self.event.full_clean()

    def test_invalid_end_date(self):
        self.event.end_date = self.event.start_date - timezone.timedelta(days=1)
        with self.assertRaises(ValidationError):
            self.event.full_clean()
