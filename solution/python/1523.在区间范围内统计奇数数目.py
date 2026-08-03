# @lc app=leetcode.cn id=1523 lang=python3


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.countOdds, (3, 7), 3)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1523 题 "在区间范围内统计奇数数目" 所有测试用例通过')
