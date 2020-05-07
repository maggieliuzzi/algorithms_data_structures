"""
Insertion Sort

Good for when a list is almost sorted
Good for small datasets
Stable
"""

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        # move elements of list[0..i-1], that are greater than key, to one position ahead of their current position 
        j = i-1
        while key < list[j] and j >= 0: # check elements to the left (from right to left) (already sorted)
            list[j + 1] = list[j]  # move one position to the right
            j -= 1  # look one left
        list[j+1] = key  # nothing smaller to the left or beginning of list
    return list


list = [3, 2, 5, 1, 7, 87, 3, 21]  # 3.5, 0, float('inf')
print(insertion_sort(list))
