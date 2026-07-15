#
# @lc app=leetcode.cn id=782 lang=python3
#
# [782] 变为棋盘
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        size = len(board)
        if any(
            board[0][0] ^ board[row][0] ^ board[0][column] ^ board[row][column]
            for row in range(size)
            for column in range(size)
        ):
            return -1

        row_ones = sum(board[0])
        column_ones = sum(row[0] for row in board)
        if (
            not size // 2 <= row_ones <= (size + 1) // 2
            or not size // 2 <= column_ones <= (size + 1) // 2
        ):
            return -1

        row_swaps = sum(board[row][0] == row % 2 for row in range(size))
        column_swaps = sum(board[0][column] == column % 2 for column in range(size))
        if size % 2:
            if row_swaps % 2:
                row_swaps = size - row_swaps
            if column_swaps % 2:
                column_swaps = size - column_swaps
        else:
            row_swaps = min(row_swaps, size - row_swaps)
            column_swaps = min(column_swaps, size - column_swaps)
        return (row_swaps + column_swaps) // 2


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.movesToChessboard,
            ([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]],),
            2,
        ),
        (solution.movesToChessboard, ([[0, 1], [1, 0]],), 0),
        (solution.movesToChessboard, ([[1, 0], [1, 0]],), -1),
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
