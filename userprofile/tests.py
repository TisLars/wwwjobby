"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from userprofile.models import CV, Vacancy


from django.test import TestCase
from django.utils import unittest
from django.test.client import Client
import random

class UserprofileTest(unittest.TestCase):
    def test_cv_list(self):
        client = Client()
        response = client.get('/cv/overview/')
        self.assertEqual(response.status_code, 200)

    def test_vacancy_list(self):
        client = Client()
        response = client.get('/vacancy/overview/')
        self.assertEqual(response.status_code, 200)
