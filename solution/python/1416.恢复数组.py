# @lc app=leetcode.cn id=1416 lang=python3


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        n = len(s)
        max_digits = len(str(k))
        dp = [0] * (n + 1)
        dp[0] = 1
        for end in range(1, n + 1):
            value = 0
            multiplier = 1
            for start in range(end - 1, max(-1, end - max_digits - 1), -1):
                value += int(s[start]) * multiplier
                if value > k:
                    break
                if s[start] != "0":
                    dp[end] = (dp[end] + dp[start]) % mod
                multiplier *= 10
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numberOfArrays, ("1000", 10000), 1),
        (solution.numberOfArrays, ("1000", 10), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1416 题 "恢复数组" 所有测试用例通过')
