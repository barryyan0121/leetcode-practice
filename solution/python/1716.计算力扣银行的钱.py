# @lc app=leetcode.cn id=1716 lang=python3


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        return (
            28 * weeks
            + 7 * weeks * (weeks - 1) // 2
            + days * (weeks + 1)
            + days * (days - 1) // 2
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.totalMoney, (4,), 10), (solution.totalMoney, (10,), 37)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1716 题 "计算力扣银行的钱" 所有测试用例通过')
