import unittest
from find_kth_largest import find_kth_largest

class TestFindKthLargest(unittest.TestCase):
    def test_find_kth_largest(self):
        input_array = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        kth_largest, position = find_kth_largest(input_array, k)
        self.assertEqual(kth_largest, 22)
        self.assertEqual(position, 2)

    def test_invalid_k(self):
        input_array = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 10
        kth_largest, position = find_kth_largest(input_array, k)
        self.assertIsNone(kth_largest)
        self.assertIsNone(position)

if name == 'main':
    unittest.main()