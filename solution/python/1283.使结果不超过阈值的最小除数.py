# @lc app=leetcode.cn id=1283 lang=python3

import os
import sys
from typing import *

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if sum((x + mid - 1) // mid for x in nums) <= threshold:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.smallestDivisor, ([1, 2, 5, 9], 6), 5),
        (solution.smallestDivisor, ([2, 3, 5, 7, 11], 11), 3),
        (solution.smallestDivisor, ([19], 5), 4),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1283 题 "使结果不超过阈值的最小除数" 所有测试用例通过')
