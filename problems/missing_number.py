"""
Missing number from array

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.
"""

# Using bit manipulation (XOR)
'''
Because we know that nums contains nn numbers and that it is missing 
exactly one number on the range [0..n-1][0..n−1], we know that nn 
definitely replaces the missing number in nums. Therefore, if we 
initialize an integer to nn and XOR it with every index and value, 
we will be left with the missing number. Consider the following example 
(the values have been sorted for intuitive convenience, but need not be):
Index	0	1	2	3
Value	0	1	3	4
Eg. len(nums) = 4
4 ^ 0 ^ 0 ^ 1 ^ 1 ^ 2 ^ 3 ^ 3 ^ 4 = 2
4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4) = 2
'''
def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = len(nums)
    for num in range(0, len(nums)):
        a ^= num ^ nums[num]
    return a