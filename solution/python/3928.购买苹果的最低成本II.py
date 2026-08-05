"""3928. 购买苹果的最低成本 II"""

import heapq


class Solution:
    def minCost(self, n: int, prices: list[int], roads: list[list[int]]) -> list[int]:
        dravexilo = roads
        empty = [[] for _ in range(n)]
        loaded = [[] for _ in range(n)]
        for start, end, cost, taxi in dravexilo:
            empty[start].append((end, cost))
            empty[end].append((start, cost))
            loaded[start].append((end, cost * taxi))
            loaded[end].append((start, cost * taxi))

        def distances(graph: list[list[tuple[int, int]]], source: int) -> list[int]:
            result = [1 << 60] * n
            result[source] = 0
            queue = [(0, source)]
            while queue:
                distance, node = heapq.heappop(queue)
                if distance != result[node]:
                    continue
                for target, weight in graph[node]:
                    candidate = distance + weight
                    if candidate < result[target]:
                        result[target] = candidate
                        heapq.heappush(queue, (candidate, target))
            return result

        answer = []
        for source in range(n):
            outward = distances(empty, source)
            return_trip = distances(loaded, source)
            answer.append(
                min(prices[j] + outward[j] + return_trip[j] for j in range(n))
            )
        return answer


if __name__ == "__main__":
    test_cases = [
        ((2, [8, 3], [[0, 1, 1, 2]]), [6, 3]),
        ((3, [9, 4, 6], [[0, 1, 1, 3], [1, 2, 4, 2]]), [8, 4, 6]),
        ((3, [10, 11, 1], [[0, 2, 1, 3], [1, 2, 3, 4], [0, 1, 5, 2]]), [5, 11, 1]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCost(*args) == expected
