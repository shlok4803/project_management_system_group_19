from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import (
    landing_view, login_view, register_view, register_view_owner, register_view_manager, register_view_employee, home_view

)

class TestURLs(TestCase):
    def test_landing_url(self):
        url = reverse('landing')
        self.assertEqual(resolve(url).func, landing_view)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_view)

    def test_register_view(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_view)

    def test_register_view_owner(self):
        url = reverse('reg_owner')
        self.assertEqual(resolve(url).func, register_view_owner)

    def test_register_view_manager(self):
        url = reverse('reg_manager')
        self.assertEqual(resolve(url).func, register_view_manager)

   