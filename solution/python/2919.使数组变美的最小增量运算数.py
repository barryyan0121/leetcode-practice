class Solution:
    def minIncrementOperations(self, nums: list[int], k: int) -> int:
        dp = [0, 0, 0]
        for value in nums:
            cost = max(0, k - value)
            dp = [dp[1], dp[2], cost + min(dp)]
        return min(dp)


assert Solution().minIncrementOperations([2, 3, 0, 0, 2], 4) == 3
