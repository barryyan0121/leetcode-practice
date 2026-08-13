class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        for x in nums:
            r = x % k
            for y in range(k):
                dp[y][r] = dp[r][y] + 1
        return max(max(row) for row in dp)


if __name__ == "__main__":
    assert Solution().maximumLength([1, 2, 3, 4, 5], 2) == 5
    assert Solution().maximumLength([1, 4, 2, 3, 1, 4], 3) == 4
