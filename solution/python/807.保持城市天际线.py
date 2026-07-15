#
# @lc app=leetcode.cn id=807 lang=python3
#
# [807] 保持城市天际线
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_maximums = list(map(max, grid))
        column_maximums = list(map(max, zip(*grid)))
        return sum(
            min(row_maximums[row], column_maximums[column]) - height
            for row, heights in enumerate(grid)
            for column, height in enumerate(heights)
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.maxIncreaseKeepingSkyline,
            ([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]],),
            35,
        ),
        (solution.maxIncreaseKeepingSkyline, ([[0, 0], [0, 0]],), 0),
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
