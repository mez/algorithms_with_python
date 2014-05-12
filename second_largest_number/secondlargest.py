#!/usr/bin/python

#finds the largest value in the array with n-1 comparisons
#finds the second largest using the results from first search to narrow the search to logn - 1 comparison
#total comparisons is n + logn - 2!
def secondLargest(array):
  #base case if length is 0 or 1
  size = len(array)
  if size == 0:
    return 0, []
  if size == 1:
    return array[0], []

  #otherwise we need to keep spliting until we get to base
  leftLargest, leftLosers = secondLargest(array[:size/2])
  rightLargest, rightLosers = secondLargest(array[size/2:])

  #at each round we need to promote the best and attach the loser to the list of defeated
  if leftLargest > rightLargest:
    #means the left is promoted, need to append right largest to the left losers list
    leftLosers.append(rightLargest)
    return leftLargest, leftLosers
  elif rightLargest > leftLargest:
    #right is promoted as the winner. add leftLargest to rightLosers and climb to next stage
    rightLosers.append(leftLargest)
    return rightLargest, rightLosers