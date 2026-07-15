#
# @lc app=leetcode.cn id=864 lang=python3
#
# [864] 获取所有钥匙的最短路径
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        target = 0
        start = None
        for row, line in enumerate(grid):
            for column, cell in enumerate(line):
                if cell == "@":
                    start = row, column
                elif cell.islower():
                    target |= 1 << (ord(cell) - ord("a"))

        queue = deque([(*start, 0, 0)])
        visited = {(*start, 0)}
        while queue:
            row, column, keys, distance = queue.popleft()
            if keys == target:
                return distance
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if not (0 <= next_row < len(grid) and 0 <= next_column < len(grid[0])):
                    continue
                cell = grid[next_row][next_column]
                if cell == "#":
                    continue
                next_keys = keys
                if cell.islower():
                    next_keys |= 1 << (ord(cell) - ord("a"))
                if cell.isupper() and not next_keys & (1 << (ord(cell) - ord("A"))):
                    continue
                state = next_row, next_column, next_keys
                if state not in visited:
                    visited.add(state)
                    queue.append((*state, distance + 1))
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.shortestPathAllKeys, (["@.a..", "###.#", "b.A.B"],), 8),
        (solution.shortestPathAllKeys, (["@..aA", "..B#.", "....b"],), 6),
        (solution.shortestPathAllKeys, (["@Aa"],), -1),
        (solution.shortestPathAllKeys, (["@"],), 0),
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
