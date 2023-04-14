import unittest 
max_integer = __import__('6-max_integer_test').max_integer_test

class TestMaxInteger(unittest.TestCase):
    """Unit tests for `max_integer_test`"""
    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        max = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(max), 200)