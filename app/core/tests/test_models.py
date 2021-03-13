from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating the new user with an email successful"""
        email = 'shantanu3250@gmail.com'
        password = 'django123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_nomalized(self):
        """test the email for new user normalized"""
        email = 'shantanu3250@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'django123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'django123')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
                'shantanu4n@gmail.com',
                'django123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
