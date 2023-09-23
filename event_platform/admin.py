from django.contrib import admin
from .models import Venue, Event


class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude")
    fields = ("name", "latitude", "longitude")


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ("event_link",)

    list_display = (
        "name",
        "venue",
        "start_date",
        "end_date",
        "ticket_price",
        "event_link",
    )
    fields = ("name", "venue", "start_date", "end_date", "ticket_price", "event_link")


# Register Venue model with the custom admin class.
admin.site.register(Venue, VenueAdmin)

# Register Event model with the custom admin class.
admin.site.register(Event, EventAdmin)  
