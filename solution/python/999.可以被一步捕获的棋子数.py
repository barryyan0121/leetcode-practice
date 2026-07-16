#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = next(
            (row, column)
            for row in range(8)
            for column in range(8)
            if board[row][column] == "R"
        )
        captures = 0
        for row_step, column_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            row, column = rook
            while 0 <= row + row_step < 8 and 0 <= column + column_step < 8:
                row += row_step
                column += column_step
                if board[row][column] == "B":
                    break
                if board[row][column] == "p":
                    captures += 1
                    break
        return captures


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.numRookCaptures,
            (
                [
                    list("........"),
                    list("...p...."),
                    list("...R...p"),
                    list("........"),
                    list("........"),
                    list("...p...."),
                    list("........"),
                    list("........"),
                ],
            ),
            3,
        ),
        (
            solution.numRookCaptures,
            (
                [
                    list("........"),
                    list(".p.p.p.."),
                    list(".p.B.p.."),
                    list(".pBRBp.."),
                    list(".p.B.p.."),
                    list(".p.p.p.."),
                    list("........"),
                    list("........"),
                ],
            ),
            0,
        ),
        (
            solution.numRookCaptures,
            ([list("R.......")] + [list("........") for _ in range(7)],),
            0,
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
