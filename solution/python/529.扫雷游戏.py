#
# @lc app=leetcode.cn id=529 lang=python3
# @lcpr version=30203
#
# [529] 扫雷游戏
#

import sys
import os
from copy import deepcopy

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        x, y = click

        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        dirs = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        def count_mines(i: int, j: int) -> int:
            total = 0
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == "M":
                    total += 1
            return total

        def dfs(i: int, j: int) -> None:
            if board[i][j] != "E":
                return
            mines = count_mines(i, j)
            if mines:
                board[i][j] = str(mines)
                return
            board[i][j] = "B"
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    dfs(ni, nj)

        dfs(x, y)
        return board


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def run_case(board: List[List[str]], click: List[int]) -> List[List[str]]:
        return solution.updateBoard(deepcopy(board), click)

    test_cases = [
        (
            run_case,
            (
                [
                    ["E", "E", "E", "E", "E"],
                    ["E", "E", "M", "E", "E"],
                    ["E", "E", "E", "E", "E"],
                    ["E", "E", "E", "E", "E"],
                ],
                [3, 0],
            ),
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "M", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
        ),
        (
            run_case,
            (
                [
                    ["B", "1", "E", "1", "B"],
                    ["B", "1", "M", "1", "B"],
                    ["B", "1", "1", "1", "B"],
                    ["B", "B", "B", "B", "B"],
                ],
                [1, 2],
            ),
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "X", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
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


#
# @lcpr case=start
# [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]\n
# [3,0]\n
# @lcpr case=end
#
