from my_list import find_max, find_min, find_average, is_sorted, reverse_list
import unittest

class MyListTest(unittest.TestCase):
    def test_find_max(self):
        """
        ทดสอบฟังก์ชัน find_max
        """
        self.assertEqual(find_max([1, 2, 3]), 3)
        self.assertEqual(find_max([5, 10, 2]), 10)
        self.assertEqual(find_max([100, 50, 25]), 100)

    def test_find_min(self):
        """
        ทดสอบฟังก์ชัน find_min
        """
        self.assertEqual(find_min([1, 2, 3]), 1)
        self.assertEqual(find_min([5, 10, 2]), 2)
        self.assertEqual(find_min([100, 50, 25]), 25)

    def test_find_average(self):
        """
        ทดสอบฟังก์ชัน find_average
        """
        self.assertEqual(find_average([4, 6, 5]), 5)

    def test_is_sorted_with_sorted_list(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted([25, 71 ,77 ,80 ]))

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])


