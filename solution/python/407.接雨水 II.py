#
# @lc app=leetcode.cn id=407 lang=python3
# @lcpr version=30203
#
# [407] 接雨水 II
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        visited = [[False] * n for _ in range(m)]
        heap = []

        for i in range(m):
            for j in (0, n - 1):
                if not visited[i][j]:
                    visited[i][j] = True
                    heapq.heappush(heap, (heightMap[i][j], i, j))
        for j in range(1, n - 1):
            for i in (0, m - 1):
                if not visited[i][j]:
                    visited[i][j] = True
                    heapq.heappush(heap, (heightMap[i][j], i, j))

        ans = 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while heap:
            h, i, j = heapq.heappop(heap)
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    nh = heightMap[ni][nj]
                    if nh < h:
                        ans += h - nh
                        heapq.heappush(heap, (h, ni, nj))
                    else:
                        heapq.heappush(heap, (nh, ni, nj))
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.trapRainWater,
            [[[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]],
            4,
        ),
        (solution.trapRainWater, [[[3, 3, 3], [3, 3, 3], [3, 3, 3]]], 0),
        (solution.trapRainWater, [[[1]]], 0),
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
# [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]\n
# @lcpr case=end

#
