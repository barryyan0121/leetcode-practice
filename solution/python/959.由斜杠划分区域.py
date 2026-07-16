#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))
        regions = len(parent)

        def find(index):
            while index != parent[index]:
                parent[index] = parent[parent[index]]
                index = parent[index]
            return index

        def union(first, second):
            nonlocal regions
            first, second = find(first), find(second)
            if first != second:
                parent[first] = second
                regions -= 1

        for row in range(n):
            for column in range(n):
                base = 4 * (row * n + column)
                if grid[row][column] != "\\":
                    union(base, base + 3)
                    union(base + 1, base + 2)
                if grid[row][column] != "/":
                    union(base, base + 1)
                    union(base + 2, base + 3)
                if row + 1 < n:
                    union(base + 2, base + 4 * n)
                if column + 1 < n:
                    union(base + 1, base + 7)
        return regions


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.regionsBySlashes, ([" /", "/ "],), 2),
        (solution.regionsBySlashes, ([" /", "  "],), 1),
        (solution.regionsBySlashes, (["/\\", "\\/"],), 5),
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
