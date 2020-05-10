"""
Move zeroes in array to the end

"""

def move_zeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    non_zeroes = 0
    for num in range(len(nums)):
        print(nums)
        if nums[num] != 0:
            nums[non_zeroes], nums[num] = nums[num], nums[non_zeroes]
            non_zeroes += 1

ls = [4, 0, 2, 0, 3, 0, 2]
ls = [0, 0, 4, 1, 0, 2]
move_zeroes(ls)
print(ls)
