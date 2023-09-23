from django.test import TestCase

from django.urls import reverse  # Import reverse function


class EventPlatformTestCase(TestCase):
    def test_event_list_view(self):
        # Test the event_list view
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
