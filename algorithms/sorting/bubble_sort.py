"""
Bubble Sort

Space Complexity: O(1)
Stable

Cons:
Time Complexity: O(n^2)
"""


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list


list = [3, 2, 5, 1, 7, 87, 3, 21]
# 2 3
print(bubble_sort(list))
