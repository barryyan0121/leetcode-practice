# @lc app=leetcode.cn id=1284 lang=python3

import os
import sys
from typing import *

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        start = sum(
            mat[r][c] << (r * cols + c) for r in range(rows) for c in range(cols)
        )
        queue = [(start, 0)]
        seen = {start}
        for state, steps in queue:
            if state == 0:
                return steps
            for r in range(rows):
                for c in range(cols):
                    nxt = state
                    for nr, nc in (
                        (r, c),
                        (r - 1, c),
                        (r + 1, c),
                        (r, c - 1),
                        (r, c + 1),
                    ):
                        if 0 <= nr < rows and 0 <= nc < cols:
                            nxt ^= 1 << (nr * cols + nc)
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, steps + 1))
        return -1


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minFlips, ([[0, 0], [0, 1]],), 3),
        (solution.minFlips, ([[0]],), 0),
        (solution.minFlips, ([[1, 1, 1], [1, 0, 1], [0, 0, 0]],), 6),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1284 题 "转化为全零矩阵的最少反转次数" 所有测试用例通过')
