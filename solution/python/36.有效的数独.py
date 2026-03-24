#
# @lc app=leetcode.cn id=36 lang=python3
# @lcpr version=30202
#
# [36] 有效的数独
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                box_idx = (r // 3) * 3 + (c // 3)
                if value in rows[r] or value in cols[c] or value in boxes[box_idx]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box_idx].add(value)

        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.isValidSudoku,
            (
                [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ],
            ),
            True,
        ),
        (
            solution.isValidSudoku,
            (
                [
                    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ],
            ),
            False,
        ),
        (
            solution.isValidSudoku,
            (
                [
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                ],
            ),
            True,
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
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end
