#
# @lc app=leetcode.cn id=130 lang=python3
# @lcpr version=30203
#
# [130] 被围绕的区域
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "S"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    board2 = [["X"]]

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.solve,
            (board1,),
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        ),
        (solution.solve, (board2,), [["X"]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            func(*args)
            result = args[0]
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
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\n
# @lcpr case=end
