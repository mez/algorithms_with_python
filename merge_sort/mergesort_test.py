#!/usr/bin/python

from mergesort import mergesort
import unittest

class TestMergeSort(unittest.TestCase):
  def setUp(self):
    self.unsortedDistinct = [3,2,1]
    self.unsortedNotDistinct = [3,2,1,3,2,1]

  def test_mergesort_with_distinct_list(self):
    sortedresult = mergesort(self.unsortedDistinct)
    self.assertEqual(sortedresult, [1,2,3])

  def test_mergesort_with_not_distinct_list(self):
    sortedresult = mergesort(self.unsortedNotDistinct)
    self.assertEqual(sortedresult, [1,1,2,2,3,3])

if __name__ == '__main__':
  unittest.main()