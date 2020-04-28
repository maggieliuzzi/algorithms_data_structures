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
        result = 0
        for i in range(0, len(str(n))):
            result += pow(int(str(n)[i]), 2)
        return result
        
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    result = isHappyHelper(n)

    if result == 1:
        #print(result)
        return True

    isHappy(result)


print(isHappy(19))
