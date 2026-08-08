from typing import List


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        size = len(arr)
        dp = [[0] * size for _ in range(size)]
        for left in range(size - 1, -1, -1):
            dp[left][left] = 1
            for right in range(left + 1, size):
                dp[left][right] = 1 + dp[left + 1][right]
                for middle in range(left + 1, right + 1):
                    if arr[left] == arr[middle]:
                        dp[left][right] = min(
                            dp[left][right],
                            (dp[left + 1][middle - 1] if middle > left + 1 else 0)
                            + (dp[middle + 1][right] if middle < right else 0),
                        )
        return dp[0][-1]


if __name__ == "__main__":
    test_cases = [([1, 3, 4, 1, 5], 3)]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().minimumMoves(arr) == expected
