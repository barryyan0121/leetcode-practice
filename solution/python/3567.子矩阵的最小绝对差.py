#
# @lc app=leetcode.cn id=3567 lang=python3
#
# [3567] 子矩阵的最小绝对差
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        ans = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]

        for top in range(rows - k + 1):
            for left in range(cols - k + 1):
                values = set()
                for r in range(top, top + k):
                    for c in range(left, left + k):
                        values.add(grid[r][c])

                ordered = sorted(values)
                if len(ordered) < 2:
                    ans[top][left] = 0
                    continue

                best = float("inf")
                for i in range(1, len(ordered)):
                    best = min(best, ordered[i] - ordered[i - 1])
                ans[top][left] = best

        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.minAbsDiff,
            ([[1, 8], [3, -2]], 2),
            [[2]],
        ),
        (
            solution.minAbsDiff,
            ([[3, -1]], 1),
            [[0, 0]],
        ),
        (
            solution.minAbsDiff,
            ([[1, 5, 3], [8, 4, 7], [2, 9, 6]], 2),
            [[1, 1], [1, 1]],
        ),
        (
            solution.minAbsDiff,
            ([[4, 4], [4, 4]], 2),
            [[0]],
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
