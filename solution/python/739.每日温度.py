#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                previous = stack.pop()
                answer[previous] = index - previous
            stack.append(index)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.dailyTemperatures,
            ([73, 74, 75, 71, 69, 72, 76, 73],),
            [1, 1, 4, 2, 1, 1, 0, 0],
        ),
        (solution.dailyTemperatures, ([30, 40, 50, 60],), [1, 1, 1, 0]),
        (solution.dailyTemperatures, ([30, 60, 90],), [1, 1, 0]),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
