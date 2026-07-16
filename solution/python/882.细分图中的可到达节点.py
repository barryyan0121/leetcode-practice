#
# @lc app=leetcode.cn id=882 lang=python3
#
# [882] 细分图中的可到达节点
#

import os
import sys
from heapq import heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = [[] for _ in range(n)]
        for first, second, nodes in edges:
            graph[first].append((second, nodes + 1))
            graph[second].append((first, nodes + 1))

        distances = [float("inf")] * n
        distances[0] = 0
        queue = [(0, 0)]
        while queue:
            distance, node = heappop(queue)
            if distance != distances[node]:
                continue
            for neighbor, weight in graph[node]:
                next_distance = distance + weight
                if next_distance < distances[neighbor] and next_distance <= maxMoves:
                    distances[neighbor] = next_distance
                    heappush(queue, (next_distance, neighbor))

        answer = sum(distance <= maxMoves for distance in distances)
        for first, second, nodes in edges:
            from_first = max(0, maxMoves - distances[first])
            from_second = max(0, maxMoves - distances[second])
            answer += min(nodes, from_first + from_second)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.reachableNodes,
            ([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3),
            13,
        ),
        (
            solution.reachableNodes,
            ([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4),
            23,
        ),
        (solution.reachableNodes, ([], 0, 1), 1),
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
