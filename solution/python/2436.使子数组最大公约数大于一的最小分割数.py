"""2436. 使子数组最大公约数大于一的最小分割数"""

from math import gcd


class Solution:
    def minimumSplits(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for end in range(1, n + 1):
            current = 0
            for start in range(end - 1, -1, -1):
                current = gcd(current, nums[start])
                if current == 1:
                    break
                dp[end] = min(dp[end], dp[start] + 1)
        return dp[n]


if __name__ == "__main__":
    test_cases = [(([12, 6, 3, 14, 8],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumSplits(*args) == expected
