"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
"""

from statistics import median

def quicksort_subroutine(nums1):
  piv_points = []
  left = []
  equal = []
  right = []

  if len(nums1) > 1:
    piv_points.append(nums1[0])
    piv_points.append(nums1[len(nums1)//2])
    piv_points.append(nums1[len(nums1)-1])
    pivot = median(piv_points)
    for nums1 in nums1:
      if nums1 < pivot:
        left.append(nums1)
      elif nums1 == pivot:
        equal.append(nums1)
      elif nums1 > pivot:
        right.append(nums1)
    return quicksort_subroutine(left) + equal + quicksort_subroutine(right)
  else:
    return nums1

def merge_and_sort(nums1, nums2):
  nums1 += nums2
  nums1 = quicksort_subroutine(nums1)
  print(nums1)
  medianvalue = median(nums1)
  return medianvalue

"""
SUCCESS
"""
