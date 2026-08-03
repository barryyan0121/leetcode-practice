# @lc app=leetcode.cn id=1413 lang=python3


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        prefix = minimum = 0
        for num in nums:
            prefix += num
            minimum = min(minimum, prefix)
        return 1 - minimum


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.minStartValue, ([-3, 2, -3, 4, 2],), 5)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1413 题 "逐步求和得到正数的最小值" 所有测试用例通过')
