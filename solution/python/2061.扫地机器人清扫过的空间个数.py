#
# @lc app=leetcode.cn id=2061 lang=python3
# @lcpr version=30203
#
# [2061] 扫地机器人清扫过的空间个数
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        rows, cols = len(room), len(room[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        seen = set()
        cleaned = set()
        row = col = direction = 0

        while (row, col, direction) not in seen:
            seen.add((row, col, direction))
            cleaned.add((row, col))
            next_row = row + directions[direction][0]
            next_col = col + directions[direction][1]
            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and room[next_row][next_col] == 0
            ):
                row, col = next_row, next_col
            else:
                direction = (direction + 1) % 4
        return len(cleaned)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numberOfCleanRooms, ([[0, 0, 0], [1, 1, 0], [0, 0, 0]],), 7),
        (solution.numberOfCleanRooms, ([[0, 1, 0], [1, 0, 0], [0, 0, 0]],), 1),
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
    print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
    sys.exit(1)
