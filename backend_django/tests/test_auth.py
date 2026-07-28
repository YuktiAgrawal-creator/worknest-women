from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_model = get_user_model()

    def test_register_and_login(self):
        # register
        res = self.client.post('/api/auth/register', {'name':'Test','email':'t@example.com','password':'secret123'})
        self.assertEqual(res.status_code, 201)
        self.assertTrue(res.data['success'])
        token = res.data['token']
        # login
        res2 = self.client.post('/api/auth/login', {'email':'t@example.com','password':'secret123'})
        self.assertEqual(res2.status_code, 200)
        self.assertTrue(res2.data['success'])
        # me
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + res2.data['token'])
        res3 = self.client.get('/api/auth/me')
        self.assertEqual(res3.status_code, 200)
        self.assertTrue(res3.data['success'])
