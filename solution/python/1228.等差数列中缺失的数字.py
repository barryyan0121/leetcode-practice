from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        difference = (arr[-1] - arr[0]) // len(arr)
        for index in range(1, len(arr)):
            expected = arr[0] + difference * index
            if arr[index] != expected:
                return expected
        return arr[0]


if __name__ == "__main__":
    test_cases = [([5, 7, 11, 13], 9), ([15, 13, 12], 14)]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().missingNumber(arr) == expected
