"""
Reverse string in-place

Given as an array
"""

def reverse(s):
    # if len(s) == 0:
        # return s
    
    # Option 1
    # s.reverse()
    # Option 2
    # s = s[::-1]
    # Option 3
    '''
    # Time: O(N) (N/2 swaps). Space: O(N) (to keep recursion stack)
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)
    helper(0, len(s) - 1)
    '''
    # Option 4
    # Time: O(N) (N/2 swaps). Space: O(1) (constant space).
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1

    # return s

s = ["h","e","l","l","o"]
# s = ["h",float('inf'),"l",2,"o"]
# s = []
reverse(s)
print(s)
