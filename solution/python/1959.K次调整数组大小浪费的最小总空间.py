"""1959. K 次调整数组大小浪费的最小总空间"""


class Solution:
    def minSpaceWastedKResizing(self, nums: list[int], k: int) -> int:
        n = len(nums)
        inf = 10**18
        dp = [[inf] * (k + 2) for _ in range(n + 1)]
        dp[0][0] = 0
        for end in range(1, n + 1):
            maximum = 0
            for start in range(end, 0, -1):
                maximum = max(maximum, nums[start - 1])
                wasted = maximum * (end - start + 1) - sum(nums[start - 1 : end])
                for changes in range(1, k + 2):
                    dp[end][changes] = min(
                        dp[end][changes], dp[start - 1][changes - 1] + wasted
                    )
        return min(dp[n])


if __name__ == "__main__":
    test_cases = [(([10, 20, 30, 40, 50], 1), 40), (([10, 20, 15, 30, 20], 2), 15)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minSpaceWastedKResizing(*args) == expected
