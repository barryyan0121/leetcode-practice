"""1937. 扣分后的最大得分"""


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        dp = points[0][:]
        for row in points[1:]:
            left = [0] * len(dp)
            best = -(10**18)
            for i, value in enumerate(dp):
                best = max(best, value + i)
                left[i] = best - i
            right = [0] * len(dp)
            best = -(10**18)
            for i in range(len(dp) - 1, -1, -1):
                best = max(best, dp[i] - i)
                right[i] = best + i
            dp = [row[i] + max(left[i], right[i]) for i in range(len(row))]
        return max(dp)


if __name__ == "__main__":
    test_cases = [(([[1, 2, 3], [1, 5, 1], [3, 1, 1]],), 9)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxPoints(*args) == expected
