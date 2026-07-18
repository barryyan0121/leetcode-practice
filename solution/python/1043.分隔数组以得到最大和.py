from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for end in range(1, len(arr) + 1):
            largest = 0
            for start in range(end - 1, max(-1, end - k - 1), -1):
                largest = max(largest, arr[start])
                dp[end] = max(dp[end], dp[start] + largest * (end - start))
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 15, 7, 9, 2, 5, 10], 3, 84),
        ([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4, 83),
        ([1], 1, 1),
    ]
    for _, (arr, k, expected) in enumerate(test_cases):
        assert solution.maxSumAfterPartitioning(arr, k) == expected
