"""
Quick Sort

Time Complexity: O(n log n) (the fastest on average)
Space Complexity: O(log(n))

Pivoting technique:
    Picking a pivot (intelligently, ideally), eg. last item in the array
    Getting pivot to its correct position in the sorted array

Cons:
Worst case: O(n^2) (when the pivot chosen happens to be the smallest or largest number in the list, 
    and therefore, the list isn't being split in half)
    If list presorted for some reason, and pivot is first or last, sorting would take a long time
"""

# Chosen pivot: last element in array
# Pivot element is placed at its correct position in sorted array
# All elements smaller than pivot are placed to the left of the pivot one and all greater ones to the right
def partition(arr, low, high):   #  Eg. [3, 2, 5, 1, 87, 3, 21, 2.5, 0, -1, 7]
    pivot = arr[high]  # pivot value
    pi = low  # partition index 
     
    for i in range(low, high): 
        if arr[i] <= pivot:  # if current element is smaller than or equal to pivot
            print("\t", arr, pi, i)
            if pi != i:
                arr[pi], arr[i] = arr[i], arr[pi]
            pi += 1  # index of smaller element

    arr[pi], arr[high] = arr[high], arr[pi] 
    return pi  # position of pivot in sorted list
  
  
def quickSort(arr, low, high):
    """
    low: start index
    high: end index
    """
    if low < high:

        pi = partition(arr, low, high)  # partitioning index. pivot now correctly placed at arr[pi]

        quickSort(arr, low, pi - 1)  # sort elements before pivot
        quickSort(arr, pi + 1, high)  # sort elements after pivot 


list = [3, 2, 5, 1, 87, 3, 21, 2.5, 0, -1, 7]
quickSort(list, 0, len(list) - 1)
print(list)
