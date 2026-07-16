#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        for row, values in enumerate(grid):
            for column, height in enumerate(values):
                if height:
                    area += 2 + height * 4
                    if row:
                        area -= 2 * min(height, grid[row - 1][column])
                    if column:
                        area -= 2 * min(height, values[column - 1])
        return area


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.surfaceArea, ([[1, 2], [3, 4]],), 34),
        (solution.surfaceArea, ([[1, 1, 1], [1, 0, 1], [1, 1, 1]],), 32),
        (solution.surfaceArea, ([[2, 2, 2], [2, 1, 2], [2, 2, 2]],), 46),
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
