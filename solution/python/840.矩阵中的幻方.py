#
# @lc app=leetcode.cn id=840 lang=python3
#
# [840] 矩阵中的幻方
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(row: int, column: int) -> bool:
            square = [grid[row + i][column : column + 3] for i in range(3)]
            return (
                sorted(sum(square, [])) == list(range(1, 10))
                and all(sum(line) == 15 for line in square)
                and all(sum(square[i][j] for i in range(3)) == 15 for j in range(3))
                and square[0][0] + square[1][1] + square[2][2] == 15
                and square[0][2] + square[1][1] + square[2][0] == 15
            )

        return sum(
            is_magic(row, column)
            for row in range(len(grid) - 2)
            for column in range(len(grid[0]) - 2)
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.numMagicSquaresInside,
            ([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]],),
            1,
        ),
        (solution.numMagicSquaresInside, ([[8]],), 0),
        (solution.numMagicSquaresInside, ([[4, 9, 2], [3, 5, 7], [8, 1, 6]],), 1),
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
