#!/usr/bin/python

from inversioncount import countInversions
import unittest
from math import factorial

#helper to generate combination count
def combination(n,k):
  numerator=factorial(n)
  denominator=(factorial(k)*factorial(n-k))
  answer=numerator/denominator
  return answer

class TestInversionCounter(unittest.TestCase):
  def setUp(self):
    self.invertedWorstCase = [6,5,4,3,2,1]
    self.noInversions = [1,2,3,4,5,6]

  def test_inversion_counter_with_worse_case_inversions(self):
    result = countInversions(self.invertedWorstCase)
    self.assertEqual(result[0], combination(len(self.invertedWorstCase),2))

  def test_inversion_counter_with_no_inversions_aka_sorted(self):
    result = countInversions(self.noInversions)
    self.assertEqual(result[0], 0)

if __name__ == '__main__':
  unittest.main()
