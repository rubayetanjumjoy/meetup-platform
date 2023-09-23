from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VenueViewSet, EventViewSet

router = DefaultRouter()
router.register(r"venues", VenueViewSet)
router.register(r"events", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
