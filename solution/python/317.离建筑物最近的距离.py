#
# @lc app=leetcode.cn id=317 lang=python3
# @lcpr version=30203
#
# [317] 离建筑物最近的距离
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import deque
from common.node import *


# @lc code=start
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]
        buildings = 0

        def bfs(sr: int, sc: int) -> None:
            visited = [[False] * n for _ in range(m)]
            queue = deque([(sr, sc, 0)])
            visited[sr][sc] = True
            while queue:
                r, c, d = queue.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        if grid[nr][nc] == 0:
                            dist[nr][nc] += d + 1
                            reach[nr][nc] += 1
                            queue.append((nr, nc, d + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += 1
                    bfs(i, j)

        ans = min(
            (
                dist[i][j]
                for i in range(m)
                for j in range(n)
                if grid[i][j] == 0 and reach[i][j] == buildings
            ),
            default=float("inf"),
        )
        return -1 if ans == float("inf") else ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.shortestDistance,
            (
                [
                    [1, 0, 2, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                ],
            ),
            7,
        ),
        (
            solution.shortestDistance,
            (
                [
                    [1, 0],
                    [0, 1],
                ],
            ),
            2,
        ),
        (
            solution.shortestDistance,
            (
                [
                    [1, 2, 0],
                ],
            ),
            -1,
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
# [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]\n
# @lcpr case=end
