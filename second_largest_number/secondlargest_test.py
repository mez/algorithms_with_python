#!/usr/bin/python

from secondlargest import secondLargest
import unittest


class TestSecondLargest(unittest.TestCase):
  def setUp(self):
    self.distinctArray = [6,5,4,3,2,1,0]

  def test_second_largest(self):
    largest, playersBeatByLargest = secondLargest(self.distinctArray)
    self.assertEqual(largest, 6)
    second_largest, playersBeatBySecondLargest = secondLargest(playersBeatByLargest)
    self.assertEqual(second_largest, 5)


if __name__ == '__main__':
  unittest.main()
