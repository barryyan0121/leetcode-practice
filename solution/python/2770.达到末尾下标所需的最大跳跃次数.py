class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        dp = [-(10**9)] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(-1, dp[-1])


if __name__ == "__main__":
    assert Solution().maximumJumps([1, 3, 6, 4, 1, 2], 2) == 3
