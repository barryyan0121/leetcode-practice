# @lc app=leetcode.cn id=1411 lang=python3


class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        same, different = 6, 6
        for _ in range(1, n):
            same, different = (3 * same + 2 * different) % mod, (
                2 * same + 2 * different
            ) % mod
        return (same + different) % mod


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.numOfWays, (1,), 12), (solution.numOfWays, (2,), 54)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1411 题 "给 N x 3 网格图涂色的方案数" 所有测试用例通过')
