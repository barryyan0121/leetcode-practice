from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        best = current = 0
        for value in arr * min(k, 2):
            current = max(0, current + value)
            best = max(best, current)
        if k > 2:
            best += max(0, sum(arr)) * (k - 2)
        return best % 1_000_000_007


if __name__ == "__main__":
    test_cases = [([1, 2], 3, 9), ([1, -2, 1], 5, 2), ([-1, -2], 7, 0)]
    for _, (arr, k, expected) in enumerate(test_cases):
        assert Solution().kConcatenationMaxSum(arr, k) == expected
