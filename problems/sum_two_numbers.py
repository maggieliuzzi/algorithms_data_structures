"""
Given a list of integers and a target integer, return the indices of the first two values whose sum is equal to the target number
# TOCHECK: any difference if sorted with this implementation?
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if type(nums) != list or len(nums) < 2:  # or (type(target) != int and type(target) != float)
        return None
    
    complements = {}
    for index in range(len(nums)):
        print(complements)
        if nums[index] in complements:
            return complements[nums[index]], index 
            
        complements[target - nums[index]] = index  # could be an issue if not all numbers


nums = [2.2, 4, 5, 6.8, 1, 15]
# nums = [4.5, 4.5]
target = 9  # issue with the target being a float because of hashing
print(twoSum(nums, target))
