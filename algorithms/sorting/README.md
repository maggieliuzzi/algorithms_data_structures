# Sorting

## Elementary
- Bubble Sort
    Time Complexity: average - worst: O(n^2)
    Space Complexity: O(1)
- Insertion Sort
    Time Complexity: average - worst: O(n^2)
    Space Complexity: O(1)
    Less commonly-used than Divide and Conquer algorithms. 
    Great if input is small or nearly sorted. 
    Easy to implement in code
- Selection Sort

## Divide and Conquer
- Merge Sort
    Time Complexity: O(n log(n))
    Space Complexity: O(n), a bit higher. Expensive for in-memory sorting, okay is off-memory/ too large to fit in memory anyway
    Commonly used. Fast, including worst case scenario. Always good time performance
    Stable
- Quick Sort
    Time Complexity: average: O(n log(n)), but worst case O(n^2) (if bad pivot)
    Space Complexity: O(log(n))
    Commonly-used
    Good when average case performance matters more than worst-case performance
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


# Real-Life Examples

Considering differences in speed, stability and readability of the algorithm, whether the input is already/nearly sorted, how large the input is, etc.

- Sorting 10 schools around your house by distance:
    Input is fairly small
    Insertion Sort (really fast in small sorts, easy to code and space complexity O(1), possibly pre/nearly sorted)

- eBay sorts listings by the current bid amount:
    Bid: eg. intigers, fix-length/ certain range: eg. 1-100, to beat that O(n log(n)) time
    Radix or counting sort
    Merge Sort

- Sport scores on ESPN:
    Decimal places, different formats, different sports
    Quick Sort (although worst place is possible, okay for in-memory sorting, merge sort has worse space complexity)

- Massive database (can't fit all into memory) needs to sort through past year's user data:
    Probably sorting externally anyway
    Merge Sort (no need to optimise for in-memory sorting, but since the data is so big, time performance is key, and Quick Sort has n^2 worst case)

- Almost-sorted Udemy review data needs to update and add 2 new reviews:
    Insertion Sort (data might be huge but assuming previous data is sorted)

- Temperature records for the past 50 years in Canada:
    If temperatures have no decimal places (eg. intigers -40 - 40, small range): Radix or Counting Sort
    Quick Sort (for efficient in-memory sorting)

- Large username database needs to be sorted. Data is very random:
    Merge Sort if we have enough memory and memory isn't too expensive
    Quick Sort if not too worried about worst case and database isn't that large, to save on memory space
    Heap Sort?

- You want to teach sorting for the first time:
    Elementary algorithms, eg. Bubble Sort, Selection Sort, Insertion Sort?
