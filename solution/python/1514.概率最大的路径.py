# @lc app=leetcode.cn id=1514 lang=python3

import heapq


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = [[] for _ in range(n)]
        for (first, second), probability in zip(edges, succProb):
            graph[first].append((second, probability))
            graph[second].append((first, probability))
        best = [0.0] * n
        best[start_node] = 1.0
        queue = [(-1.0, start_node)]
        while queue:
            negative_probability, node = heapq.heappop(queue)
            probability = -negative_probability
            if node == end_node:
                return probability
            if probability < best[node]:
                continue
            for neighbor, edge_probability in graph[node]:
                candidate = probability * edge_probability
                if candidate > best[neighbor]:
                    best[neighbor] = candidate
                    heapq.heappush(queue, (-candidate, neighbor))
        return 0.0


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.maxProbability,
            (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2),
            0.25,
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert abs(func(*args) - expected) < 1e-9
    print('第 1514 题 "概率最大的路径" 所有测试用例通过')
