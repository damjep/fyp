from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email='user@example.com', password='testpass', name='Test User')
        self.assertEqual(user.email, 'user@example.com')
        self.assertTrue(user.check_password('testpass'))
        self.assertEqual(user.role, User.Role.EMPLOYEE)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        admin = User.objects.create_superuser(email='admin@example.com', password='adminpass', name='Admin User')
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)
        self.assertEqual(admin.role, User.Role.EMPLOYEE) 

    def test_user_str(self):
        user = User.objects.create_user(email='user2@example.com', password='testpass', name='Another User')
        self.assertEqual(str(user), 'user2@example.com')

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='nopass')

from shifts.models import Shift  # Assuming shifts app

class UserShiftTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='staff@example.com', password='staffpass')
        self.shift = Shift.objects.create(days='Monday', shift_start=9 , shift_end=17)

    def test_add_shift(self):
        self.user.shift_available.add(self.shift)
        self.assertIn(self.shift, self.user.shift_available.all())