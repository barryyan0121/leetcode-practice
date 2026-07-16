#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        size = len(board)

        def destination(square):
            row_from_bottom, column = divmod(square - 1, size)
            row = size - row_from_bottom - 1
            if row_from_bottom % 2:
                column = size - column - 1
            return board[row][column]

        queue = deque([(1, 0)])
        visited = {1}
        while queue:
            square, moves = queue.popleft()
            for reached in range(square + 1, min(square + 6, size * size) + 1):
                next_square = destination(reached)
                if next_square == -1:
                    next_square = reached
                if next_square == size * size:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.snakesAndLadders,
            (
                [
                    [-1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1],
                    [-1, 35, -1, -1, 13, -1],
                    [-1, -1, -1, -1, -1, -1],
                    [-1, 15, -1, -1, -1, -1],
                ],
            ),
            4,
        ),
        (solution.snakesAndLadders, ([[-1, -1], [-1, 3]],), 1),
        (solution.snakesAndLadders, ([[1, 1, -1], [1, 1, 1], [-1, 1, 1]],), -1),
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
