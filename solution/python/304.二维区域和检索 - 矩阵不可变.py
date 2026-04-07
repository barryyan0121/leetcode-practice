#
# @lc app=leetcode.cn id=304 lang=python3
# @lcpr version=30203
#
# [304] 二维区域和检索 - 矩阵不可变
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    self.prefix[r][c + 1]
                    + self.prefix[r + 1][c]
                    - self.prefix[r][c]
                    + matrix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )


# @lc code=end


if __name__ == "__main__":
    def run_operations(ops: List[str], values: List[List[int]]) -> List[Optional[int]]:
        obj = None
        result = []

        for op, value in zip(ops, values):
            if op == "NumMatrix":
                obj = NumMatrix(value)
                result.append(None)
            else:
                result.append(obj.sumRegion(*value))
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"],
                [
                    [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]],
                    [2, 1, 4, 3],
                    [1, 1, 2, 2],
                    [1, 2, 2, 4],
                ],
            ),
            [None, 8, 11, 12],
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
# ["NumMatrix","sumRegion","sumRegion","sumRegion"]\n[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]\n
# @lcpr case=end
