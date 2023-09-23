from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Venue, Event


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    # Use StringRelatedField for the venue field to display the venue name
    venue = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = "__all__"

    def to_representation(self, instance):
        # Convert the ticket_price to a float for serialization
        representation = super(EventSerializer, self).to_representation(instance)
        representation["ticket_price"] = float(representation["ticket_price"])
        return representation
