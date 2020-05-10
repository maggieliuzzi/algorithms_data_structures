"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.
"""

def fizz_buzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    '''
    Option 1: Time: O(n), Space: O(n)
    if n == 0:
        return []
    repr = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            repr.append("FizzBuzz")
        elif i % 3 == 0:
            repr.append("Fizz")
        elif i % 5 == 0:
            repr.append("Buzz")
        else:
            repr.append(str(i))
    return repr
    '''
    # Option 2 (string concatenation): same time and space complexity, but cleaner when new conditions added)
    '''
    # if n == 0:  # not necessary
        # return []
    repr = []
    for i in range(1, n+1):
        item = ""
        if i % 3 == 0:
            item += "Fizz"
        if i % 5 == 0:
            item += "Buzz"
        if item == "":  # if not item:
            item += str(i)
        repr.append(item)
    return repr
    '''
    # Option 3 (hashing the conditions): same time and space complexity, but clearner with many conditions
    map = {
        3: "Fizz",
        5: "Buzz"
    }
    repr = []
    for i in range(1, n+1):
        item = ""
        for cond in map:
            if i % cond == 0:
                item += map[cond]
        if item == "":  # if not item:
            item += str(i)
        repr.append(item)
    return repr

print(fizz_buzz(0))
print(fizz_buzz(1))
print(fizz_buzz(4))
print(fizz_buzz(15))
