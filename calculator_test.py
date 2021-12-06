import unittest 
from calculator import td_sum
from calculator import td_divide
from calculator import td_multiply
from calculator import td_sub

class MyTestCase(unittest.TestCase):
    def test_td_sum(self):
        self.assertEqual(td_sum(1, 2), 3)

    def test_td_divide(self):
        self.assertEqual(td_divide(10, 5), 2)
    
    def test_td_multiply(self):
        self.assertEqual(td_multiply(5, 2), 10)
    
    def test_td_sub(self):
        self.assertEqual(td_sub(10, 10), 0)

if __name__ == '__main__':
    unittest.main()