#
# @lc app=leetcode.cn id=499 lang=python3
# @lcpr version=30203
#
# [499] 迷宫 III
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findShortestWay(
        self, maze: List[List[int]], ball: List[int], hole: List[int]
    ) -> str:
        m, n = len(maze), len(maze[0])
        dirs = [(-1, 0, "u"), (0, -1, "l"), (0, 1, "r"), (1, 0, "d")]
        start = (0, "", ball[0], ball[1])
        heap = [start]
        best = {(ball[0], ball[1]): (0, "")}

        while heap:
            dist, path, x, y = heapq.heappop(heap)
            if [x, y] == hole:
                return path
            if best.get((x, y), (float("inf"), "~")) < (dist, path):
                continue
            for dx, dy, ch in dirs:
                nx, ny, step = x, y, 0
                while (
                    0 <= nx + dx < m
                    and 0 <= ny + dy < n
                    and maze[nx + dx][ny + dy] == 0
                ):
                    nx += dx
                    ny += dy
                    step += 1
                    if [nx, ny] == hole:
                        break
                cand = (dist + step, path + ch)
                prev = best.get((nx, ny))
                if prev is None or cand < prev:
                    best[(nx, ny)] = cand
                    heapq.heappush(heap, (cand[0], cand[1], nx, ny))
        return "impossible"


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findShortestWay,
            (
                [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                ],
                [0, 0],
                [2, 2],
            ),
            "dr",
        ),
        (
            solution.findShortestWay,
            (
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [0, 0],
                [1, 1],
            ),
            "impossible",
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
# [[0,0,0],[0,0,0],[0,0,0]]\n[0,0]\n[2,2]\n
# @lcpr case=end

#
