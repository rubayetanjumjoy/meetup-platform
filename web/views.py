from event_platform.models import Event, Venue
from django.shortcuts import render


def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    context = {"event": event}
    return render(request, "events/event_detail.html", context)


def event_list(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, "events/home.html", context)
