#
# @lc app=leetcode.cn id=505 lang=python3
# @lcpr version=30203
#
# [505] 迷宫 II
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def shortestDistance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        m, n = len(maze), len(maze[0])
        dist = [[float("inf")] * n for _ in range(m)]
        sx, sy = start
        dx, dy = destination
        dist[sx][sy] = 0
        pq = [(0, sx, sy)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            d, x, y = heapq.heappop(pq)
            if d != dist[x][y]:
                continue
            if [x, y] == destination:
                return d
            for dx_step, dy_step in directions:
                nx, ny, steps = x, y, 0
                while (
                    0 <= nx + dx_step < m
                    and 0 <= ny + dy_step < n
                    and maze[nx + dx_step][ny + dy_step] == 0
                ):
                    nx += dx_step
                    ny += dy_step
                    steps += 1
                nd = d + steps
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))

        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.shortestDistance,
            (
                [
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                ],
                [0, 4],
                [4, 4],
            ),
            12,
        ),
        (
            solution.shortestDistance,
            (
                [
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                ],
                [0, 4],
                [3, 2],
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
# maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n
# @lcpr case=end
#
