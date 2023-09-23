from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Venue, Event
from .serializers import VenueSerializer, EventSerializer


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    pagination_class = PageNumberPagination  #  pagination
    filter_backends = [filters.OrderingFilter]  #  ordering
    ordering_fields = ["name"]  # Specify fields for ordering
    http_method_names = ["get"]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related("venue")
    serializer_class = EventSerializer
    pagination_class = PageNumberPagination  #  pagination
    filter_backends = [filters.OrderingFilter]  #  ordering
    ordering_fields = [
        "name",
        "start_date",
        "end_date",
        "ticket_price",
    ]
    http_method_names = ["get"]

    @action(detail=False, methods=["GET"])
    def search(self, request):
        # Retrieve the 'search' query parameter from the request URL
        search_query = request.query_params.get("search", "")

        # Perform a case-insensitive search for events by name
        queryset = Event.objects.filter(name__icontains=search_query)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
