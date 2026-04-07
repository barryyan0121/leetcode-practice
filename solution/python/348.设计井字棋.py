#
# @lc app=leetcode.cn id=348 lang=python3
# @lcpr version=30203
#
# [348] 设计井字棋
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0

    def move(self, row: int, col: int, player: int) -> int:
        value = 1 if player == 1 else -1
        self.rows[row] += value
        self.cols[col] += value
        if row == col:
            self.diag += value
        if row + col == self.n - 1:
            self.anti += value
        if (
            abs(self.rows[row]) == self.n
            or abs(self.cols[col]) == self.n
            or abs(self.diag) == self.n
            or abs(self.anti) == self.n
        ):
            return player
        return 0


# @lc code=end


if __name__ == "__main__":
    def run_operations(ops: List[str], values: List[List[int]]) -> List[Optional[int]]:
        obj = None
        result = []

        for op, value in zip(ops, values):
            if op == "TicTacToe":
                obj = TicTacToe(value[0])
                result.append(None)
            else:
                result.append(obj.move(*value))
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"],
                [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]],
            ),
            [None, 0, 0, 0, 0, 0, 0, 1],
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
# ["TicTacToe","move","move","move","move","move","move","move"]\n[[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]\n
# @lcpr case=end
