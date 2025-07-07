# Selection Sort

Selection Sort is a simple and intuitive sorting algorithm that divides the input list into two parts: a sorted part and an unsorted part. It repeatedly selects the smallest (or largest, depending on the order) element from the unsorted part and moves it to the end of the sorted part.

## How it works

1. Start with an empty sorted part and the entire list as the unsorted part.
2. Find the smallest element in the unsorted part.
3. Swap it with the first element of the unsorted part.
4. Move the boundary between the sorted and unsorted parts one element to the right.
5. Repeat steps 2-4 until the unsorted part is empty.
6. The sorted part now contains all elements in order.

## Complexity

- **Time Complexity**: O(n^2) in the worst and average cases, O(n) in the best case (when the array is already sorted).
- **Space Complexity**: O(1) since it sorts the array in place without requiring additional storage.
