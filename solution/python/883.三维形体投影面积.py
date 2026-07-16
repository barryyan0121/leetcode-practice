#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum(height > 0 for row in grid for height in row)
        front = sum(max(row) for row in grid)
        side = sum(max(column) for column in zip(*grid))
        return top + front + side


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.projectionArea, ([[1, 2], [3, 4]],), 17),
        (solution.projectionArea, ([[2]],), 5),
        (solution.projectionArea, ([[1, 0], [0, 2]],), 8),
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
