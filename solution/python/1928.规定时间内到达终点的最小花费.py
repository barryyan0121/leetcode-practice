"""1928. 规定时间内到达终点的最小花费"""

import heapq


class Solution:
    def minCost(
        self, maxTime: int, edges: list[list[int]], passingFees: list[int]
    ) -> int:
        graph = [[] for _ in passingFees]
        for start, end, travel_time in edges:
            graph[start].append((end, travel_time))
            graph[end].append((start, travel_time))
        best = [[10**18] * (maxTime + 1) for _ in passingFees]
        best[0][0] = passingFees[0]
        heap = [(passingFees[0], 0, 0)]
        while heap:
            cost, time, node = heapq.heappop(heap)
            if cost != best[node][time]:
                continue
            if node == len(passingFees) - 1:
                return cost
            for target, duration in graph[node]:
                next_time = time + duration
                if next_time <= maxTime:
                    next_cost = cost + passingFees[target]
                    if next_cost < best[target][next_time]:
                        best[target][next_time] = next_cost
                        heapq.heappush(heap, (next_cost, next_time, target))
        return -1


if __name__ == "__main__":
    test_cases = [
        (
            (
                30,
                [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
                [5, 1, 2, 20, 20, 3],
            ),
            11,
        ),
        (
            (
                29,
                [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
                [5, 1, 2, 20, 20, 3],
            ),
            48,
        ),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCost(*args) == expected
