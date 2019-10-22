from django.test import TestCase
from app.calc import add, subtract


class calcTests(TestCase):
    # All the names of test functions need to have "test" as their prefix
    def test_add_numbers(self):
        """unit test for add function"""
        self.assertEqual(add(5, 6), 11)

    def test_subtract_numbers(self):
        """unit test for subtract function"""
        self.assertEqual(subtract(3, 2), 1)
