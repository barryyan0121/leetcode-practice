#
# @lc app=leetcode.cn id=417 lang=python3
# @lcpr version=30203
#
# [417] 太平洋大西洋水流问题
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *

from collections import deque


# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def bfs(starts: List[Tuple[int, int]]) -> set[Tuple[int, int]]:
            seen = set(starts)
            q = deque(starts)
            while q:
                x, y = q.popleft()
                for nx, ny in (
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1),
                ):
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and (nx, ny) not in seen
                        and heights[nx][ny] >= heights[x][y]
                    ):
                        seen.add((nx, ny))
                        q.append((nx, ny))
            return seen

        pacific_starts = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        atlantic_starts = [(m - 1, j) for j in range(n)] + [
            (i, n - 1) for i in range(m)
        ]
        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)
        return [list(cell) for cell in pacific & atlantic]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.pacificAtlantic,
            (
                [
                    [1, 2, 2, 3, 5],
                    [3, 2, 3, 4, 4],
                    [2, 4, 5, 3, 1],
                    [6, 7, 1, 4, 5],
                    [5, 1, 1, 2, 4],
                ],
            ),
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        (solution.pacificAtlantic, ([[1]],), [[0, 0]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert sorted(map(tuple, result)) == sorted(map(tuple, expected))
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
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]\n
# @lcpr case=end

#
