"""2547. 拆分数组的最小代价"""


class Solution:
    def minCost(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0] + [10**18] * n
        for right in range(1, n + 1):
            counts = {}
            trimmed = 0
            for left in range(right, 0, -1):
                value = nums[left - 1]
                count = counts.get(value, 0)
                if count == 1:
                    trimmed += 2
                elif count >= 2:
                    trimmed += 1
                counts[value] = count + 1
                dp[right] = min(dp[right], dp[left - 1] + k + trimmed)
        return dp[n]


if __name__ == "__main__":
    test_cases = [(([1, 2, 1, 2, 1, 3, 3], 2), 8)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCost(*args) == expected
