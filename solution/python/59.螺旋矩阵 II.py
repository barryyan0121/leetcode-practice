#
# @lc app=leetcode.cn id=59 lang=python3
# @lcpr version=30202
#
# [59] 螺旋矩阵 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        value = 1

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                matrix[top][c] = value
                value += 1
            top += 1

            for r in range(top, bottom + 1):
                matrix[r][right] = value
                value += 1
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    matrix[bottom][c] = value
                    value += 1
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    matrix[r][left] = value
                    value += 1
                left += 1

        return matrix


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.generateMatrix,
            (3,),
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
        ),
        (solution.generateMatrix, (1,), [[1]]),
        (
            solution.generateMatrix,
            (4,),
            [
                [1, 2, 3, 4],
                [12, 13, 14, 5],
                [11, 16, 15, 6],
                [10, 9, 8, 7],
            ],
        ),
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
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# 3\n
# @lcpr case=end
