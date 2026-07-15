#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

import heapq
import os
import sys
from collections import defaultdict
from typing import *


# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((time, target))
        distances = {}
        heap = [(0, k)]
        while heap:
            distance, node = heapq.heappop(heap)
            if node in distances:
                continue
            distances[node] = distance
            for time, neighbor in graph[node]:
                if neighbor not in distances:
                    heapq.heappush(heap, (distance + time, neighbor))
        return max(distances.values()) if len(distances) == n else -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.networkDelayTime, ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
        (solution.networkDelayTime, ([[1, 2, 1]], 2, 1), 1),
        (solution.networkDelayTime, ([[1, 2, 1]], 2, 2), -1),
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
