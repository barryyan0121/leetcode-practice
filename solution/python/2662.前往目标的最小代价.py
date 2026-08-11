#
# @lc app=leetcode.cn id=2662 lang=python3
# @lcpr version=30203
#
# [2662] 前往目标的最小代价
#

import heapq
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minimumCost(
        self,
        start: List[int],
        target: List[int],
        specialRoads: List[List[int]],
    ) -> int:
        points = [[road[2], road[3]] for road in specialRoads]
        distances = [float("inf")] * len(points)
        for index, road in enumerate(specialRoads):
            distances[index] = (
                abs(start[0] - road[0]) + abs(start[1] - road[1]) + road[4]
            )
        answer = abs(start[0] - target[0]) + abs(start[1] - target[1])
        heap = [(distance, index) for index, distance in enumerate(distances)]
        heapq.heapify(heap)
        while heap:
            distance, index = heapq.heappop(heap)
            if distance != distances[index]:
                continue
            current = points[index]
            answer = min(
                answer,
                distance + abs(current[0] - target[0]) + abs(current[1] - target[1]),
            )
            for road_index, road in enumerate(specialRoads):
                walk = abs(current[0] - road[0]) + abs(current[1] - road[1])
                candidate = distance + walk + road[4]
                if candidate < distances[road_index]:
                    distances[road_index] = candidate
                    heapq.heappush(heap, (candidate, road_index))
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumCost([1, 1], [4, 5], [[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]]) == 5
    assert (
        solution.minimumCost(
            [3, 2],
            [5, 7],
            [[5, 7, 3, 2, 1], [3, 2, 3, 4, 4], [3, 3, 5, 5, 5], [3, 4, 5, 6, 6]],
        )
        == 7
    )
    print("测试用例通过")
