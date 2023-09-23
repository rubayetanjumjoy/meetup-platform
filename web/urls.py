from django.urls import path
from . import views

urlpatterns = [
    path("event-detail/<int:event_id>/", views.event_detail, name="event_information"),
    path("web/", views.event_list, name="home"),
]
