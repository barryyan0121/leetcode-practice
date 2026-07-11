#
# @lc app=leetcode.cn id=688 lang=python3
# @lcpr version=30203
#
# [688] 骑士在棋盘上的概率
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from functools import lru_cache
from common.node import *


# @lc code=start
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        @lru_cache(None)
        def dfs(step: int, r: int, c: int) -> float:
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0.0
            if step == 0:
                return 1.0
            return sum(dfs(step - 1, r + dr, c + dc) for dr, dc in moves) / 8.0

        return dfs(k, row, column)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.knightProbability, (3, 2, 0, 0), 0.0625),
        (solution.knightProbability, (1, 0, 0, 0), 1.0),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert abs(result - expected) < 1e-9
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)
