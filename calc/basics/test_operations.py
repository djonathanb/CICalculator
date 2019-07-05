"""
Unit tests for the operations library
"""

from unittest import TestCase

from calc.basics import operations


class TestOperations(TestCase):

    def test_addition(self):
        self.assertEqual(operations.add(2, 2), 4)

    def test_subtraction(self):
        self.assertEqual(operations.subtract(4, 2), 2)

    def test_multiplication(self):
        self.assertEqual(operations.multiply(10, 10), 100)
