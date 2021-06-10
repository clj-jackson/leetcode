# Leetcode 1. Two Sum
# Difficulty - Easy

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
----------------------------------------------------------------
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
----------------
Example 2:
----------------
Input: nums = [3,2,4], target = 6
Output: [1,2]
----------------
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

def twosum(num_list, target):
  i = 0
  x = True
  while x == True:
    value2 = target - num_list[i]
    if value2 in num_list:
      x = False
      value2 = num_list.index(value2)
      return [i, value2]
    i += 1

print(twosum([2,7,11,15], 26))

"""
SUCCESS
"""
