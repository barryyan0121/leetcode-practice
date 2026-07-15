#
# @lc app=leetcode.cn id=741 lang=python3
#
# [741] 摘樱桃
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        size = len(grid)
        impossible = -(10**9)
        dp = [[impossible] * size for _ in range(size)]
        dp[0][0] = grid[0][0]

        for step in range(1, 2 * size - 1):
            next_dp = [[impossible] * size for _ in range(size)]
            low, high = max(0, step - size + 1), min(size - 1, step)
            for first_row in range(low, high + 1):
                first_column = step - first_row
                if grid[first_row][first_column] == -1:
                    continue
                for second_row in range(low, high + 1):
                    second_column = step - second_row
                    if grid[second_row][second_column] == -1:
                        continue
                    best = dp[first_row][second_row]
                    if first_row:
                        best = max(best, dp[first_row - 1][second_row])
                    if second_row:
                        best = max(best, dp[first_row][second_row - 1])
                    if first_row and second_row:
                        best = max(best, dp[first_row - 1][second_row - 1])
                    if best == impossible:
                        continue
                    cherries = grid[first_row][first_column]
                    if first_row != second_row:
                        cherries += grid[second_row][second_column]
                    next_dp[first_row][second_row] = best + cherries
            dp = next_dp
        return max(0, dp[-1][-1])


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.cherryPickup, ([[0, 1, -1], [1, 0, -1], [1, 1, 1]],), 5),
        (solution.cherryPickup, ([[1, 1, -1], [1, -1, 1], [-1, 1, 1]],), 0),
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
