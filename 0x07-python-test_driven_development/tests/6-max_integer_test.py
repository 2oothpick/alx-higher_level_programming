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

        def test_one_negative(self):
            """Tests for list with one negative number"""
            max = [200, 10, 8, -36, 14, 50]
            self.assertEqual(max_integer(max), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        max = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(max), -1)

    def test_one_element(self):
        """Tests for list with only one element"""
        max = [1]
        self.assertEqual(max_integer(max), 1)

    def test_no_args(self):
        """Tests for no arguments passed to function"""
        self.assertIsNone(max_integer())  
    

if __name__ == "__main__":
    unittest.main()