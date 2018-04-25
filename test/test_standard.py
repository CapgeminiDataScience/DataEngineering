from unittest import TestCase


class TestStandard(TestCase):

    def test_addition(self):
        value_one = 1
        value_two = 2
        self.assertEquals(3, value_one + value_two)
