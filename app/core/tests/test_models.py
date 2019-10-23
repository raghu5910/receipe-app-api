from django.tests import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ tests email and passowrd"""
        email = "raghu@gmail.com"
        password = "hello"

        user = get_user_model.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email of a new user is normalized"""
        email = "raghu@GMAIL.com"

        user = get_user_model.objects.create_user(email=email, password="test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model.objects.create_user(email=None, password="test123")
