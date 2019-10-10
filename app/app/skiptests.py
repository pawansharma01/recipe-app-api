from django.test import TestCase

from app.calc import addNums, subtractNums

"""
Added 'skip' at the beginning of this script name to avoid it being
picked up for tests run - when you want to use again remove it !!!
"""


class CalcTests(TestCase):

    def test_add_numbers(self):
        """
        Test two numbers can be added together
        """
        self.assertEqual(addNums(3, 8), 11)

    def test_subtract_numbers(self):
        """
        TDD: test subtracting two numbers together
        """
        self.assertEqual(subtractNums(5, 11), 6)
