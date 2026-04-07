#
# @lc app=leetcode.cn id=490 lang=python3
# @lcpr version=30203
#
# [490] 迷宫
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import deque
from common.node import *


# @lc code=start
class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        m, n = len(maze), len(maze[0])
        q = deque([tuple(start)])
        seen = {tuple(start)}
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            if [x, y] == destination:
                return True
            for dx, dy in dirs:
                nx, ny = x, y
                while (
                    0 <= nx + dx < m
                    and 0 <= ny + dy < n
                    and maze[nx + dx][ny + dy] == 0
                ):
                    nx += dx
                    ny += dy
                if (nx, ny) not in seen:
                    seen.add((nx, ny))
                    q.append((nx, ny))
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.hasPath,
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
            True,
        ),
        (
            solution.hasPath,
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
            False,
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
# [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n[0,4]\n[4,4]\n
# @lcpr case=end

#
