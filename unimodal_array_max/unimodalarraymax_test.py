#!/usr/bin/python

from unimodalarraymax import unimodalmax
import unittest

class TestUnimodalArrayMaxElement(unittest.TestCase):
  def setUp(self):
    self.unimodalarray = [1,6,5,4,2]

  def test_unimodal_array_max_element_finder(self):
    maxElement = unimodalmax(self.unimodalarray)
    self.assertEqual(maxElement, 6)


if __name__ == '__main__':
  unittest.main()
