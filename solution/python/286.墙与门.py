#
# @lc app=leetcode.cn id=286 lang=python3
# @lcpr version=30203
#
# [286] 墙与门
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import deque
from common.node import *


# @lc code=start
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == 2147483647:
                    rooms[ni][nj] = rooms[i][j] + 1
                    q.append((ni, nj))
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    INF = 2147483647
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.wallsAndGates,
            [
                [
                    [INF, -1, 0, INF],
                    [INF, INF, INF, -1],
                    [INF, -1, INF, -1],
                    [0, -1, INF, INF],
                ]
            ],
            [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]],
        ),
        (solution.wallsAndGates, [[[]]], [[]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            rooms = args[0]
            func(*args)
            assert rooms == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {rooms}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {rooms}"
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
# [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]\n
# @lcpr case=end

#
