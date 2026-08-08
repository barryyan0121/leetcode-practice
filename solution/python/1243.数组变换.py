from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            next_arr = arr[:]
            for index in range(1, len(arr) - 1):
                if arr[index] < arr[index - 1] and arr[index] < arr[index + 1]:
                    next_arr[index] += 1
                elif arr[index] > arr[index - 1] and arr[index] > arr[index + 1]:
                    next_arr[index] -= 1
            if next_arr == arr:
                return arr
            arr = next_arr


if __name__ == "__main__":
    test_cases = [([6, 2, 3, 4], [6, 3, 3, 4])]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().transformArray(arr) == expected
