#!/usr/bin/python

from arrayindexelementfinder import doAnyElementMatchIndex
import unittest

class TestUnimodalArrayMaxElement(unittest.TestCase):
  def setUp(self):
    #given a sorted (from smallest to largest) array A of n distinct integers
    #which can be positive, negative, or zero.
    self.array = [-1,0,2,3]
    self.no_match_array = [1,2,3,4]

  def test_search_with_match(self):
    result = doAnyElementMatchIndex(self.array)
    self.assertEqual(result, True)

  def test_search_with_no_match(self):
    result = doAnyElementMatchIndex(self.no_match_array)
    self.assertEqual(result, False)


if __name__ == '__main__':
  unittest.main()
