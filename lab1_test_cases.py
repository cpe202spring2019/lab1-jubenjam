import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """check for ValueError"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        """check for when one value is max"""
        self.assertEqual(max_list_iter([1, 3, 2]), 3)
        self.assertEqual(max_list_iter([2, 1.5, 1]), 2)
        self.assertEqual(max_list_iter([1, 1.4, 1.5]), 1.5)
        """check for when multiple values are max"""
        self.assertEqual(max_list_iter([1, 1.5, 1.5]), 1.5)
        self.assertEqual(max_list_iter([1, 1, 0.5]), 1)
        self.assertEqual(max_list_iter([2, 1, 2]), 2)
        """check for when all values are equal"""
        self.assertEqual(max_list_iter([2, 2, 2]), 2)
        """check for empty list"""
        self.assertEqual(max_list_iter([]), None)

    def test_reverse_rec(self):
        """check for ValueError"""
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        """check max value in various places"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,3,2]),[2,3,1])
        self.assertEqual(reverse_rec([4,3,2]),[2,3,4])
        """check empty list"""
        self.assertEqual(reverse_rec([]),[])
        """check two same values"""
        self.assertEqual(reverse_rec([2,3,2]),[2,3,2])
        self.assertEqual(reverse_rec([3,3,2]),[2,3,3])
        self.assertEqual(reverse_rec([1,3,3]),[3,3,1])
        """check all same value"""
        self.assertEqual(reverse_rec([3,3,3]),[3,3,3])

    def test_bin_search(self):
        """check for Value Error"""
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(3, 3, 4, tlist)
        """check searching entire list"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        """check when searching part of a list"""
        self.assertEqual(bin_search(4, 3, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(4, 6, high, list_val), None)
        self.assertEqual(bin_search(4, 1, 3, list_val), None)
        """check when value is at end of designated section"""
        self.assertEqual(bin_search(4, 4, high, list_val), 4)
        self.assertEqual(bin_search(10, 3, len(list_val)-1, list_val), 8)
        """check when value is not the same as the index"""
        self.assertEqual(bin_search(4, 3, 10, [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11]), 4) 

if __name__ == "__main__":
        unittest.main()

    
