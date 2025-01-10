# from django.test import TestCase
import time
from rest_framework.test import APITestCase # Extends Django's TestCase
from rest_framework import status
from django.core import mail

class NotifyAPITest(APITestCase):

    def test_notify_sales(self):
        """ Test that a notification is sent to the sales channel """

        response = self.client.post('/api/notify/', {
            "topic": "sales",
            "description": "A little message for sales"
        }, format='json')
        # Checks that the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Checks that the response contains the success message
        self.assertIn("Notification sent successfully", response.data['message'])

    def test_notify_pricing(self):
        """ Test that a notification is sent to the pricing channel """
        
        response = self.client.post('/api/notify/', {
            "topic": "pricing",
            "description": "A little message for pricing"
        }, format='json')
        # Checks that the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Checks that the response contains the success message
        self.assertIn("Notification sent successfully", response.data['message'])

    def test_notify_unknown_topic(self):
        """ Test that a notification is not sent with an unknown topic """
        
        response = self.client.post('/api/notify/', {
            "topic": "unknown",
            "description": "A little message for an unknown topic"
        }, format='json')
        # Checks that the response is 404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Checks that the response contains the error message
        self.assertIn("Topic 'unknown' not registered", response.data['message'])

    def test_notify_missing_fields(self):
        """ Test that the request fails if fields are missing """

        response = self.client.post('/api/notify/', {}, format='json')
        # Checks that the response is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Checks that the response contains the error messages
        self.assertIn("topic", response.data)
        self.assertIn("description", response.data)

    def test_notify_invalid_fields(self):
        """ Test that the request fails if fields are invalid """

        response = self.client.post('/api/notify/', {
            "topic": "sales",
            "description": "a" * 1001 # Exceeds the max_length
        }, format='json')
        # Checks that the response is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Checks that the response contains the error messages
        self.assertIn("description", response.data)

