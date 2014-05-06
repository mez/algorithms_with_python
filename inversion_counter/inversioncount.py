#!/usr/bin/python

#this will take a list and return a counter for the number of inversions + sorted version of the list
#return (inverstionCount, sortedList)
def countInversions(array):
  #base case if array of size 0 or 1, we are done!
  size = len(array)
  if size == 1 or size == 0:
    return 0, array

  #recurse away!
  leftCount, left = countInversions(array[:size/2])
  rightCount, right = countInversions(array[(size/2):])
  splitCount, final = countSplitInversionAndMerge(left, right)
  #count inversions all the way back up
  return (leftCount+rightCount+splitCount), final


def countSplitInversionAndMerge(left, right):
  merged = [] #start with an empty list
  count = 0
  #while i have elements in left or right keep going
  while len(left) != 0 or len(right) != 0:
    #check if one of the sides is empty, if so just append remaining to merged and break
    if len(left) == 0 and len(right) != 0:
      merged+=right
      break
    elif len(left) != 0 and len(right) == 0:
      merged+=left
      break
    else:
      #means that there are elements in both sides
      #walk through the both left and right and pop smallest..
      #value btw left[0] or right[0] and append into merged
      if left[0] < right[0]:
        merged.append(left[0]);left.pop(0)
      elif left[0] > right[0]:
        merged.append(right[0]);right.pop(0)
        #means that there was an inversion!
        count+=len(left)
      elif left[0] == right[0]:
        merged.append(left[0]);left.pop(0)
        merged.append(right[0]);right.pop(0)
  return count, merged

