#
# @lc app=leetcode.cn id=2906 lang=python3
#
# [2906] 构造乘积矩阵
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        rows, cols = len(grid), len(grid[0])
        total = rows * cols
        values = [grid[r][c] % mod for r in range(rows) for c in range(cols)]

        suffix = [1] * (total + 1)
        for i in range(total - 1, -1, -1):
            suffix[i] = suffix[i + 1] * values[i] % mod

        ans = [[0] * cols for _ in range(rows)]
        prefix = 1
        for i, value in enumerate(values):
            ans[i // cols][i % cols] = prefix * suffix[i + 1] % mod
            prefix = prefix * value % mod

        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.constructProductMatrix,
            ([[1, 2], [3, 4]],),
            [[24, 12], [8, 6]],
        ),
        (
            solution.constructProductMatrix,
            ([[12345], [2], [3]],),
            [[6], [0], [0]],
        ),
        (
            solution.constructProductMatrix,
            ([[7, 5, 2]],),
            [[10, 14, 35]],
        ),
        (
            solution.constructProductMatrix,
            ([[3, 10, 7], [5, 6, 4], [8, 9, 2]],),
            [[12135, 4875, 12255], [9750, 12240, 6015], [9180, 8160, 12030]],
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
