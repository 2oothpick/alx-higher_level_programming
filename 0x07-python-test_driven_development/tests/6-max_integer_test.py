import unittest 
max_integer = __import__('6-max_integer_test').max_integer_test

class TestMaxInteger(unittest.TestCase):
    """Unit tests for `max_integer_test`"""
    def test_positive_beginning(self):
        """Test for maximum value at the beginning of list"""
        max = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(max), 200)

    def test_positive_end(self):
        """Tests formaximum value at the end of list"""
        max = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(max), 50)
    
    def test_positive_middle(self):
        """Tests for maximum value at the middle of list"""
        max = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(max), 360)    

if __name__ == "__main__":
    unittest.main()