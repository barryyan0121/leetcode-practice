#
# @lc app=leetcode.cn id=803 lang=python3
#
# [803] 打砖块
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        rows, columns = len(grid), len(grid[0])
        roof = rows * columns
        parent = list(range(roof + 1))
        sizes = [1] * (roof + 1)

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(first: int, second: int) -> None:
            first, second = find(first), find(second)
            if first == second:
                return
            if sizes[first] < sizes[second]:
                first, second = second, first
            parent[second] = first
            sizes[first] += sizes[second]

        remaining = [row[:] for row in grid]
        removed = []
        for row, column in hits:
            removed.append(remaining[row][column] == 1)
            remaining[row][column] = 0

        def connect(row: int, column: int) -> None:
            node = row * columns + column
            if row == 0:
                union(node, roof)
            for row_change, column_change in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row, next_column = row + row_change, column + column_change
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and remaining[next_row][next_column]
                ):
                    union(node, next_row * columns + next_column)

        for row in range(rows):
            for column in range(columns):
                if remaining[row][column]:
                    connect(row, column)

        answer = [0] * len(hits)
        for index in range(len(hits) - 1, -1, -1):
            if not removed[index]:
                continue
            row, column = hits[index]
            before = sizes[find(roof)]
            remaining[row][column] = 1
            connect(row, column)
            answer[index] = max(0, sizes[find(roof)] - before - 1)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.hitBricks, ([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]), [2]),
        (solution.hitBricks, ([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]), [0, 0]),
        (solution.hitBricks, ([[1]], [[0, 0], [0, 0]]), [0, 0]),
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
