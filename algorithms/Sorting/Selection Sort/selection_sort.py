from typing import List


def selection_sort(nums: List):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
        print(f"Pass {i + 1}: {nums}")
    return nums


def main():
    nums = [64, 25, 12, 22, 11]
    print("Unsorted array:", nums)
    sorted_nums = selection_sort(nums)
    print("Sorted array:", sorted_nums)


if __name__ == "__main__":
    main()
