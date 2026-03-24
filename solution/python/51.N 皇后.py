#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30202
#
# [51] N 皇后
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [["."] * n for _ in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                results.append(["".join(line) for line in board])
                return

            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = "Q"

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return results


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(boards: List[List[str]]) -> List[List[str]]:
        return sorted(boards)

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.solveNQueens,
            (4,),
            [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
        ),
        (solution.solveNQueens, (1,), [["Q"]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            normalized_result = normalize(result)
            normalized_expected = normalize(expected)
            assert normalized_result == normalized_expected
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
# 4\n
# @lcpr case=end
