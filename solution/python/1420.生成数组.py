# @lc app=leetcode.cn id=1420 lang=python3


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        for maximum in range(1, m + 1):
            dp[maximum][1] = 1
        for _ in range(1, n):
            next_dp = [[0] * (k + 1) for _ in range(m + 1)]
            for cost in range(1, k + 1):
                prefix = 0
                for maximum in range(1, m + 1):
                    prefix = (prefix + dp[maximum - 1][cost - 1]) % mod
                    next_dp[maximum][cost] = (
                        maximum * dp[maximum][cost] + prefix
                    ) % mod
            dp = next_dp
        return sum(dp[maximum][k] for maximum in range(1, m + 1)) % mod


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numOfArrays, (2, 3, 1), 6),
        (solution.numOfArrays, (5, 2, 3), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1420 题 "生成数组" 所有测试用例通过')
