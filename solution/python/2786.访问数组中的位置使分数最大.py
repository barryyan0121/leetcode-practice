class Solution:
    def maxScore(self, nums: list[int], x: int) -> int:
        dp = [-(10**18), -(10**18)]
        dp[nums[0] % 2] = nums[0]
        for value in nums[1:]:
            parity = value % 2
            dp[parity] = max(dp[parity], dp[1 - parity] - x) + value
        return max(dp)


if __name__ == "__main__":
    assert Solution().maxScore([2, 3, 6, 1, 9, 2], 5) == 13
