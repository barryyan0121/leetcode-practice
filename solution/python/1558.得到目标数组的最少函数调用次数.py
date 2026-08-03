# @lc app=leetcode.cn id=1558 lang=python3


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        increments = sum(value.bit_count() for value in nums)
        shifts = max((value.bit_length() for value in nums), default=0) - 1
        return increments + max(shifts, 0)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minOperations, ([1, 5],), 5),
        (solution.minOperations, ([2, 2],), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1558 题 "得到目标数组的最少函数调用次数" 所有测试用例通过')
