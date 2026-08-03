# @lc app=leetcode.cn id=1287 lang=python3

import os
import sys
from typing import *

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        step = len(arr) // 4
        for i in range(len(arr) - step):
            if arr[i] == arr[i + step]:
                return arr[i]
        return arr[0]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findSpecialInteger, ([1, 2, 2, 6, 6, 6, 6, 7, 10],), 6),
        (solution.findSpecialInteger, ([1, 1],), 1),
        (solution.findSpecialInteger, ([1, 2, 3, 3],), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1287 题 "有序数组中出现次数超过25%的元素" 所有测试用例通过')
