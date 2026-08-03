# @lc app=leetcode.cn id=1460 lang=python3


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return sorted(target) == sorted(arr)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.canBeEqual, ([1, 2, 3, 4], [2, 4, 1, 3]), True)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1460 题 "通过翻转子数组使两个数组相等" 所有测试用例通过')
