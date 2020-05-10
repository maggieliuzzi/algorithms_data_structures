"""
Array with two elements repeated in different proportions. Find the majority one.

Eg. [1, 2, 1] >> 1
"""

# from collections import Counter

def majority_element(nums):
    counts = {}
    for i in nums:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    # counts = Counter(nums)
    return max(counts, key=counts.get)

nums = [1, 2, 1]
print(majority_element(nums))
