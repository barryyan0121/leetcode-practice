#
# @lc app=leetcode.cn id=794 lang=python3
#
# [794] 有效的井字游戏
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = sum(row.count("X") for row in board)
        o_count = sum(row.count("O") for row in board)

        def wins(player: str) -> bool:
            return (
                any(
                    all(board[row][column] == player for column in range(3))
                    for row in range(3)
                )
                or any(
                    all(board[row][column] == player for row in range(3))
                    for column in range(3)
                )
                or all(board[index][index] == player for index in range(3))
                or all(board[index][2 - index] == player for index in range(3))
            )

        x_wins = wins("X")
        o_wins = wins("O")
        return (
            x_count in (o_count, o_count + 1)
            and (not x_wins or x_count == o_count + 1)
            and (not o_wins or x_count == o_count)
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.validTicTacToe, (["O  ", "   ", "   "],), False),
        (solution.validTicTacToe, (["XOX", " X ", "   "],), False),
        (solution.validTicTacToe, (["XOX", "O O", "XOX"],), True),
        (solution.validTicTacToe, (["XXX", "OOX", "OOX"],), True),
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
