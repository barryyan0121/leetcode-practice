#
# @lc app=leetcode.cn id=2812 lang=python3
# @lcpr version=30203
#
# [2812] 找出最安全路径
#

import heapq
import os
import sys
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distance = [[-1] * n for _ in range(n)]
        queue = deque()
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    distance[row][col] = 0
                    queue.append((row, col))
        while queue:
            row, col = queue.popleft()
            for next_row, next_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    0 <= next_row < n
                    and 0 <= next_col < n
                    and distance[next_row][next_col] == -1
                ):
                    distance[next_row][next_col] = distance[row][col] + 1
                    queue.append((next_row, next_col))

        best = [[-1] * n for _ in range(n)]
        best[0][0] = distance[0][0]
        heap = [(-distance[0][0], 0, 0)]
        while heap:
            negative_safety, row, col = heapq.heappop(heap)
            safety = -negative_safety
            if (row, col) == (n - 1, n - 1):
                return safety
            if safety != best[row][col]:
                continue
            for next_row, next_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if 0 <= next_row < n and 0 <= next_col < n:
                    next_safety = min(safety, distance[next_row][next_col])
                    if next_safety > best[next_row][next_col]:
                        best[next_row][next_col] = next_safety
                        heapq.heappush(heap, (-next_safety, next_row, next_col))
        return 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 0
    assert solution.maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]) == 2
    print("测试用例通过")
