"""2915. 和为目标值的最长子序列长度"""


class Solution:
    def lengthOfLongestSubsequence(self, nums: list[int], target: int) -> int:
        dp = [-(10**9)] * (target + 1)
        dp[0] = 0
        for value in nums:
            for total in range(target, value - 1, -1):
                dp[total] = max(dp[total], dp[total - value] + 1)
        return max(dp[target], -1)


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubsequence([1, 2, 3, 4, 5], 9) == 3
