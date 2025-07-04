from typing import List


def bubble_sort(nums: List):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            print(f"Pass {i + 1}, Step {j + 1}: {nums}")
    return nums


def main():
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", nums)
    sorted_nums = bubble_sort(nums)
    print("Sorted array:", sorted_nums)


if __name__ == "__main__":
    main()

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Stable Sort: Yes
# In-Place Sort: Yes
# Best Case: O(n) when the array is already sorted
# Worst Case: O(n^2) when the array is sorted in reverse order
# Average Case: O(n^2)
