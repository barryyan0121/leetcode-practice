#
# @lc app=leetcode.cn id=2282 lang=python3
# @lcpr version=30203
#
# [2282] 在一个网格中可以看到的人数
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        answer = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            stack = []
            for col in range(cols - 1, -1, -1):
                height = heights[row][col]
                visible = 0
                while stack and stack[-1] < height:
                    stack.pop()
                    visible += 1
                answer[row][col] = visible + bool(stack)
                if stack and stack[-1] == height:
                    stack.pop()
                stack.append(height)

        for col in range(cols):
            stack = []
            for row in range(rows - 1, -1, -1):
                height = heights[row][col]
                visible = 0
                while stack and stack[-1] < height:
                    stack.pop()
                    visible += 1
                answer[row][col] += visible + bool(stack)
                if stack and stack[-1] == height:
                    stack.pop()
                stack.append(height)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.seePeople, ([[3, 1, 4, 2, 5]],), [[2, 1, 2, 1, 0]]),
        (solution.seePeople, ([[5, 1], [3, 1], [4, 1]],), [[3, 1], [2, 1], [1, 0]]),
        (solution.seePeople, ([[4, 2, 1, 1, 3]],), [[2, 2, 1, 1, 0]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
    sys.exit(1)
