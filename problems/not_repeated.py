"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""

'''
def not_repeated(ls):

    seen = {}
    for item in ls:
        if item not in seen:
            seen[item] = 1      # seen[item] if not seen[item]
        else:
            seen[item] = 2

    for item in seen:
        if seen[item] != 2:
            return item
'''      
'''
def not_repeated(ls):

    if len(ls) == 1:
        return ls[0]

    ls.sort()
    for index in range(1, len(ls)+1, 2):
        if ls[index-1] != ls[index]:
            return ls[index-1]
        
        if index == len(ls) - 2:  # len(ls) will always be odd
            if ls[index] != ls[index+1]:
                return ls[index+1]
'''

def not_repeated(nums):
    # Option 1
    if len(nums) == 0:
        return
    if len(nums) == 1:
        return nums[0]
    seen = {}
    for item in nums:
        if item in seen:
            del seen[item]
        else:
            seen[item] = 1
    return list(seen.keys())[0]
    # Option 2 (Maths): O(n)|O(n)
    # 2*(a+b+c)−(a+a+b+b+c)=c
    # return 2 * sum(set(nums)) - sum(nums)
    '''
    # Option 3 (Bit Manipulation): O(n)|O(1)
    # If we take XOR of zero and some bit, it will return that bit
    # a XOR 0 = a
    # If we take XOR of two same bits, it will return 0
    # a XOR a = 0
    # a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b
    # So we can XOR all bits together to find the unique number.
    a = 0
    for i in nums:
        a ^= i
    return a
    '''


#ls = [2,2,1]
#ls = [4,1,2,1,2]
ls = [1,2,3,1,2]
#ls = [6]
#ls = ['a', 'b', 'a']
#ls = []
print(not_repeated(ls))
