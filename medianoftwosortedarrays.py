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

def median_list(nums):
  length = len(nums)
  if length % 2 == 0:
    midpoint_upper = nums[length//2]
    midpoint_lower = nums[length//2 - 1]
    median = (midpoint_lower + midpoint_upper)/2
  else:
    median = nums[length//2]
  return median

def quicksort_subroutine(nums1):
  piv_points = []
  left = []
  equal = []
  right = []

  if len(nums1) > 1:
    piv_points.append(nums1[0])
    piv_points.append(nums1[len(nums1)//2])
    piv_points.append(nums1[len(nums1)-1])
    pivot = median_list(piv_points)
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
  nums = quicksort_subroutine(nums1)
  return nums

nums = merge_and_sort([1,2],[3,4])

print(median_list(nums))

"""
SUCCESS
"""
