# Sorting

## Elementary
- Bubble Sort
    Time Complexity: average - worst: O(n^2)
    Space Complexity: O(1)
- Insertion Sort
    Time Complexity: average - worst: O(n^2)
    Space Complexity: O(1)
    Less commonly-used than Divide and Conquer algorithms. Good if input is small or mostly sorted. Easy to implement in code
- Selection Sort

## Divide and Conquer
- Merge Sort
    Time Complexity: O(n log(n))
    Space Complexity: O(n), expensive for in-memory sorting
    Commonly used. Fast, including worst case scenario
- Quick Sort
    Time Complexity: average: O(n log(n)), but worst case O(n^2) (if bad pivot)
    Space Complexity: O(log(n))
    Commonly-used
- Heap Sort
    Time Complexity: average and worst: O(n log(n)). However, typically somewhat slower than Quick Sort
    Space Complexity: O(1), in-place
    Good if you're worried about worst case and memory

## Non-Comparison
(Some only work with fixed-length intigers in a restricted range. Makes used of binary representation in memory. Some argue they end up being pretty slow or n log(n) in practice)
- Counting Sort
    Time: average: O(n+k)
    Space: O(k)
- Radix Sort
    Time: average: O(nk)
    Space: O(n+k)
- Bucket Sort
    Time: average: O(n+k)
    Space: O(n)
