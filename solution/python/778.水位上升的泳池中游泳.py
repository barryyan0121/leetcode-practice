#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#

import os
import sys
from heapq import heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        size = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        while heap:
            time, row, column = heappop(heap)
            if row == column == size - 1:
                return time
            for row_change, column_change in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_change
                next_column = column + column_change
                if (
                    0 <= next_row < size
                    and 0 <= next_column < size
                    and (next_row, next_column) not in seen
                ):
                    seen.add((next_row, next_column))
                    heappush(
                        heap,
                        (max(time, grid[next_row][next_column]), next_row, next_column),
                    )
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.swimInWater, ([[0, 2], [1, 3]],), 3),
        (
            solution.swimInWater,
            (
                [
                    [0, 1, 2, 3, 4],
                    [24, 23, 22, 21, 5],
                    [12, 13, 14, 15, 16],
                    [11, 17, 18, 19, 20],
                    [10, 9, 8, 7, 6],
                ],
            ),
            16,
        ),
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
