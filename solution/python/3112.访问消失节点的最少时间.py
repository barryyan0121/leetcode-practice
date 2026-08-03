import heapq


class Solution:
    def minimumTime(
        self, n: int, edges: list[list[int]], disappear: list[int]
    ) -> list[int]:
        graph = [[] for _ in range(n)]
        for start, end, weight in edges:
            graph[start].append((end, weight))
            graph[end].append((start, weight))

        distance = [float("inf")] * n
        distance[0] = 0
        queue = [(0, 0)]
        while queue:
            current_time, node = heapq.heappop(queue)
            if current_time != distance[node]:
                continue
            for neighbor, weight in graph[node]:
                arrival = current_time + weight
                if arrival < disappear[neighbor] and arrival < distance[neighbor]:
                    distance[neighbor] = arrival
                    heapq.heappush(queue, (arrival, neighbor))
        return [-1 if value == float("inf") else value for value in distance]


if __name__ == "__main__":
    test_cases = [
        (3, [[0, 1, 2], [1, 2, 1], [0, 2, 4]], [1, 3, 5], [0, 2, 3]),
        (3, [[0, 1, 2], [1, 2, 1]], [1, 1, 1], [0, -1, -1]),
    ]
    for _, (n, edges, disappear, expected) in enumerate(test_cases):
        assert Solution().minimumTime(n, edges, disappear) == expected
