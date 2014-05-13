#!/usr/bin/python


###
#You are given a sorted (from smallest to largest) array A of n distinct integers
#which can be positive, negative, or zero. You want to decide whether or not there
#is an index i such that A[i] = i.
#Design the fastest algorithm that you can for solving this problem.
###

#Facts
#1. Array is sorted
#2. non repeating elements

#Given Facts - a modified binary search will yield a result in logn time.

#Takes an array with properties above
#returns True or False if array[i] = i exists
def doAnyElementMatchIndex(array):
  #recurse and cut in half each round
  result = search(array, 0, len(array)-1)
  return result

def search(array, leftIndex, rightIndex):
  #base case is hit if left and right index are the same
  if leftIndex == rightIndex:
    return array[0] == leftIndex

  #find the midindex and compare with element at midindex
  midIndex = (leftIndex+rightIndex)/2

  if array[midIndex] < midIndex:
    #means we need to move right since we know index will always increase
    return search(array, midIndex+1, rightIndex)
  elif array[midIndex] > midIndex:
    #means we need to move left since we know element will always increase
    return search(array, leftIndex, midIndex-1)
  else:
    #means it matches!
    return True



