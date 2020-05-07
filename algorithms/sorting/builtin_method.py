"""
Python's built-in sorting methods
"""

letters = ["b", "a", "f", "z", "m"]
words = ["amen", "calor", "baby", "zebra", "ala", "á", "b"]
numbers = [3, 6, 1, 67, 8, 99, 9, 54, 4, 5]


print(sorted(letters))
print(sorted(words))
print(sorted(numbers))

letters.sort()
words.sort()
numbers.sort()

print(" ")
print(letters)
print(words)
print(numbers)
