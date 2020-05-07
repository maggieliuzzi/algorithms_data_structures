"""
Selection Sort

Space Complexity: O(1)

Cons:
Time Complexity: O(n^2)
Unstable?
"""

def selection_sort(list):
    for i in range(len(list)):
        min = i
        temp = list[i]
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                min = j
        list[i] = list[min]
        list[min] = temp
    return list

list = [3, 2, 5, 1, 7, 87, 3, 21]
print(selection_sort(list))
