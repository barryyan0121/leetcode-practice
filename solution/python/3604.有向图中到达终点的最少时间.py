"""3604. 有向图中到达终点的最少时间"""

from heapq import heappop, heappush


class Solution:
    def minTime(self, n: int, edges: list[list[int]]) -> int:
        dalmurecio = edges
        graph = [[] for _ in range(n)]
        for start, end, begin, finish in dalmurecio:
            graph[start].append((end, begin, finish))
        distance = [1 << 60] * n
        distance[0] = 0
        queue = [(0, 0)]
        while queue:
            time, node = heappop(queue)
            if time != distance[node]:
                continue
            if node == n - 1:
                return time
            for target, begin, finish in graph[node]:
                departure = max(time, begin)
                if departure <= finish and departure + 1 < distance[target]:
                    distance[target] = departure + 1
                    heappush(queue, (distance[target], target))
        return -1


if __name__ == "__main__":
    test_cases = [
        ((3, [[0, 1, 0, 1], [1, 2, 2, 5]]), 3),
        ((4, [[0, 1, 0, 3], [1, 3, 7, 8], [0, 2, 1, 5], [2, 3, 4, 7]]), 5),
        ((3, [[1, 0, 1, 3], [1, 2, 3, 5]]), -1),
    ]
    for _, ((n, edges), expected) in enumerate(test_cases):
        assert Solution().minTime(n, edges) == expected
