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
    print("\n\t--> ", arr)
    i = low - 1           # index of smaller element 
    pivot = arr[high]     # pivot 
    print("\n\tPivot: ", pivot, "\n")
  
    for j in range(low, high): 
        # if current element is smaller than or equal to pivot 
        if arr[j] <= pivot: 
            i += 1  # incrementing index of smaller element
            print(i, j)
            print(arr[i], arr[j])
            arr[i], arr[j] = arr[j], arr[i] 
            print(arr[i], arr[j]); print(" ")
    
    print(list)
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    print(list)
    return i + 1  # new position of the pivot
  
  
def quickSort(arr, low, high):
    """
    low: start index
    high: end index
    """
    if low < high: 
  
        # pi is partitioning index, arr[p] is now at the right place 
        pi = partition(arr, low, high) 
  
        # separately sort elements before partition and after partition 
        quickSort(arr, low, pi - 1) 
        quickSort(arr, pi + 1, high) 
  

list = [3, 2, 5, 1, 87, 3, 21, 2.5, 0, -1, 7]
n = len(list) 
quickSort(list, 0, n-1)
print(list)
