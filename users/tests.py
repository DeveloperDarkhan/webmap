from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CustomUser

from django.utils import timezone

# Create your tests here.

class TestCustomUserModel(TestCase):

    def setUp(self):
        self.model = CustomUser
        self.user = get_user_model().objects.create_user(
            username = 'Darkhan',
            email = 'darkhan@online.kz',
            password = 'Darkhan'
        )
        self.admin_user = get_user_model().objects.create_superuser(
            username = 'darkhan_engineer',
            email = 'd@gmail.com',
            password = '45004920'
        )

    def test_create_superuser(self):
        admin = self.admin_user
        self.assertEqual(admin.username, 'darkhan_engineer')
        self.assertEqual(admin.email, 'd@gmail.com')
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_create_user(self):
        user = self.user
        self.assertEqual(user.username, 'Darkhan')
        self.assertFalse(user.is_superuser)

class TestHomePage(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    
