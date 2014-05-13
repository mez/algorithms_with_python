#!/usr/bin/python

###
#You are a given a unimodal array of n distinct elements,
#meaning that its entries are in increasing order up until its maximum element,
#after which its elements are in decreasing order.
#Give an algorithm to compute the maximum element that runs in O(log n) time.
###


#solution was inspired using the bisection method https://www.youtube.com/watch?v=Y2AUhxoQ-OQ

#the idea is to cut the search space by half each time to give logn comparisons!

#the array has to be unimodal to have the correct properties
def unimodalmax(array):
  size = len(array)

  #1. pick left and right edges like bisection method
  leftEdgeIndex = 0
  midpointIndex = (size)/2
  rightEdgeIndex = size-1

  maximum = None
  while True:
    left = array[midpointIndex-1]
    mid = array[midpointIndex]
    right = array[midpointIndex+1]

    #check which direction to go in the array, unless we have reached max
    if left < mid and mid < right:
      #means we still need to climb the mountain!
      leftEdgeIndex = midpointIndex
      midpointIndex = (midpointIndex+rightEdgeIndex)/2
    elif left > mid and mid > right:
      #means we need to climb down
      rightEdgeIndex = midpointIndex
      midpointIndex = (midpointIndex+leftEdgeIndex)/2
    else:
      #we have found max element because the pattern of the unimodal broke.
      #in terms of bisection method there has been a change in sign. hence we have found
      #the root
      maximum = array[midpointIndex]
      break

  return maximum
