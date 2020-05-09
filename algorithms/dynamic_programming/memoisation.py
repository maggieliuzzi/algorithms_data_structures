"""
Memoisation

Caching the return value of a function called with certain parameters
"""

def add_80(value):
    return value + 80

cache = {}
def memoised_add_80(value):
    if value in cache:
        return cache[value]  # O(1)
    else:
        print("Calculation which might take a long time")
        cache[value] = value + 80  # or add_80(value)
        return cache[value]

def memoised_add_80_with_closure():
    cache_with_closure = {}
    def memoised(value):
        if value in cache_with_closure:
            return cache_with_closure[value]  # O(1)
        else:
            print("Calculation which might take a long time")
            cache_with_closure[value] = value + 80  # or add_80(value)
            return cache_with_closure[value]
    return memoised

print(memoised_add_80(5))
print(memoised_add_80(5))
print(memoised_add_80(5))
print(memoised_add_80(6))
print(memoised_add_80(6))
print("")

memoised = memoised_add_80_with_closure()  # memoised = memoised function
print(memoised(5))
print(memoised(5))
print(memoised(5))
print(memoised(6))
print(memoised(6))
print("")


def fibonacci():
    calc_count = 0
    def fibonacci_result(n):  # Time Complexity: O(2^n), but Space Complexity: O(tree height) (max, since it adds and pops functions from the stack)
        if n < 2:
            return n
        nonlocal calc_count
        calc_count += 1
        print("num calculations: ", calc_count)
        return fibonacci(n - 2) + fibonacci(n - 1)
    return fibonacci_result

def fibonacci_memoised():
    calc_count = 0
    cache = {}
    def fibonacci_result(n):  # Time Complexity: O(n), Space Complexity: O(n) (new variable)
        if n < 2:
            return n
        if n in cache:
            return cache[n]
        nonlocal calc_count
        calc_count += 1
        print("num calculations: ", calc_count)
        cache[n] = fibonacci(n - 2) + fibonacci(n - 1)
        # print(cache)
        return cache[n]
    return fibonacci_result

fibonacci = fibonacci()
# print(fibonacci(0))
# print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(5))
print("")

fibonacci = fibonacci_memoised()
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(5))
