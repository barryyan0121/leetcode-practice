# @lc app=leetcode.cn id=1365 lang=python3

from bisect import bisect_left
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        return [bisect_left(ordered, value) for value in nums]


if __name__ == "__main__":
    test_cases = [
        (Solution().smallerNumbersThanCurrent, ([8, 1, 2, 2, 3],), [4, 0, 1, 1, 3]),
        (Solution().smallerNumbersThanCurrent, ([6, 5, 4, 8],), [2, 1, 0, 3]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1365 题 "有多少小于当前数字的数字" 所有测试用例通过')
