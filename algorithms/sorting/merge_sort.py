"""
Merge Sort

Time Complexity: O(n log n)
Stable: original order of repeated items is maintained

Cons:
Space Complexity: O(n)
"""


def merge_helper(left, right):
    sorted = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted.append(left[left_index])
            left_index += 1
        else:
            sorted.append(right[right_index])
            right_index += 1
    return sorted + left[left_index:] + right[right_index:]

def merge_sort(list):
    if len(list) == 1:
        return list
    # splitting list into left and right
    length = len(list)
    middle = length // 2  # round(length / 2)
    left = list[:middle]
    right = list[middle:]
    return merge_helper(merge_sort(left), merge_sort(right))


list = [3, 2, 5, 1, 7, 87, 3, 21, 2.5]
print(merge_sort(list))
