#
# @lc app=leetcode.cn id=1594 lang=python3
#
# [1594] 矩阵的最大非负积
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        max_dp = [[0] * cols for _ in range(rows)]
        min_dp = [[0] * cols for _ in range(rows)]
        max_dp[0][0] = min_dp[0][0] = grid[0][0]

        for c in range(1, cols):
            value = max_dp[0][c - 1] * grid[0][c]
            max_dp[0][c] = value
            min_dp[0][c] = value

        for r in range(1, rows):
            value = max_dp[r - 1][0] * grid[r][0]
            max_dp[r][0] = value
            min_dp[r][0] = value

        for r in range(1, rows):
            for c in range(1, cols):
                cur = grid[r][c]
                candidates = (
                    max_dp[r - 1][c] * cur,
                    min_dp[r - 1][c] * cur,
                    max_dp[r][c - 1] * cur,
                    min_dp[r][c - 1] * cur,
                )
                max_dp[r][c] = max(candidates)
                min_dp[r][c] = min(candidates)

        ans = max_dp[-1][-1]
        return ans % mod if ans >= 0 else -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxProductPath, ([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]],), -1),
        (solution.maxProductPath, ([[1, -2, 1], [1, -2, 1], [3, -4, 1]],), 8),
        (solution.maxProductPath, ([[1, 3], [0, -4]],), 0),
        (solution.maxProductPath, ([[-1, 4, 3], [2, -5, 2]],), 40),
        (solution.maxProductPath, ([[1]],), 1),
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
