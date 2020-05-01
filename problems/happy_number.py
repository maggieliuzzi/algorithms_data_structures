"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number 
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:
    Input: 19
    Output: true
    Explanation: 
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
"""

def isHappyHelper(n):
    if len(str(n)) < 2:
        return pow(n, 2)
    else:
        result = 0
        for i in range(0, len(str(n))):
            result += pow(int(str(n)[i]), 2)
        return result
        
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    n = isHappyHelper(n)

    if n == 1:
        return True
    elif n == 4:
        return False
    
    return isHappy(n)


print(isHappy(19))
print(isHappy(28))
print(isHappy(37))
print(isHappy(2))
print(isHappy(11))
