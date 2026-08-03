# @lc app=leetcode.cn id=1449 lang=python3


class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        dp = [None] * (target + 1)
        dp[0] = ""
        for total in range(1, target + 1):
            for digit in range(9, 0, -1):
                previous = total - cost[digit - 1]
                if previous >= 0 and dp[previous] is not None:
                    candidate = dp[previous] + str(digit)
                    if dp[total] is None or (len(candidate), candidate) > (
                        len(dp[total]),
                        dp[total],
                    ):
                        dp[total] = candidate
        return dp[target] or "0"


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.largestNumber, ([4, 3, 2, 5, 6, 7, 2, 5, 5], 9), "7772")]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1449 题 "数位成本和为目标值的最大数字" 所有测试用例通过')
