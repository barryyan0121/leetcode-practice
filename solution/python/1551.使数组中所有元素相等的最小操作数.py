# @lc app=leetcode.cn id=1551 lang=python3


class Solution:
    def minOperations(self, n: int) -> int:
        return n * n // 4


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minOperations, (3,), 2),
        (solution.minOperations, (6,), 9),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1551 题 "使数组中所有元素相等的最小操作数" 所有测试用例通过')
