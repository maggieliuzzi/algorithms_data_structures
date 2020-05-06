"""
Factorial and Fibonacci

Recursive vs iterative

Recursive:
DRY (helps not to repeat yourself)
Readability
Maintains state at different levels of recursion
But extra memory footprint (space complexity): larger stack because of additional function calls, adding functions to 
    the call stack, potentially stack overlow, take up stack space
        > This can be solved with Tail Call Optimisation

When to use?
    - Typically useful when dealing with trees or graphs traversals, sometimes when sorting (merge sort and quick sort)
    - A problem that can be divided in subproblems
    - All instances of subproblem is identical in nature
    - Those solutions can be combined to solve the larger problem
"""

def factorial_recursive(num):  # O(n)
    if num <= 2:
        if num == 0:
            return 1
        return num
    return num * factorial_recursive(num - 1)


def factorial_iterative(num):  # O(n)
    if num <= 2:
        if num == 0:
            return 1
        return num
    factorial = num  # factorial = 1 and then range(2, num+1)
    for i in range(num - 1, 1, -1):  # from num - 1 til 2 inclusive
        factorial *= i
    return factorial


print(factorial_recursive(5))
print(factorial_iterative(5))

print(factorial_recursive(0))
print(factorial_iterative(0))


# 0, 1, 2, 3, 4, 5, 6,  7,  8
# 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci_recursive(index):  # O(2^n), exponential time --> sometimes turned into (O(n) with memoization or dynamic programming
    if index < 2:
        return index
    return fibonacci_recursive(index - 2) + fibonacci_recursive(index - 1)


def fibonacci_iterative(index):  # O(n)
    ''' Memory: O(n)
    arr = [0, 1]
    for i in range(2, index + 1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[index]
    '''
    if index < 2:
        return index
    second_last = 0
    last = 1
    for i in range(2, index + 1):
        sum = second_last + last
        second_last = last
        last = sum
    return sum


print(fibonacci_iterative(6))
print(fibonacci_recursive(6))  # a lot slower


def reverse_string_recursive(string):
    if len(string) == 0:
        return string
    return string[-1] + reverse_string_recursive(string[:-1])


def reverse_string_iterative(string):
    '''
    string_list = list(reversed(list(string)))
    string = ""
    for letter in string_list:
        string += letter
    return string
    '''
    reversed = ""
    for char in range(len(list(string)) - 1, -1, -1):
        reversed += string[char]
    return reversed


print(reverse_string_recursive("lala ! o"))
print(reverse_string_iterative("lala ! o"))
print(reverse_string_recursive(""))
print(reverse_string_iterative(""))

def lala():
    lala()

lala()