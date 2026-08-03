import heapq


class Solution:
    def findAnswer(self, n: int, edges: list[list[int]]) -> list[bool]:
        graph = [[] for _ in range(n)]
        for index, (start, end, weight) in enumerate(edges):
            graph[start].append((end, weight, index))
            graph[end].append((start, weight, index))

        def distances(source: int) -> list[int]:
            result = [10**30] * n
            result[source] = 0
            queue = [(0, source)]
            while queue:
                distance, node = heapq.heappop(queue)
                if distance != result[node]:
                    continue
                for neighbor, weight, _ in graph[node]:
                    candidate = distance + weight
                    if candidate < result[neighbor]:
                        result[neighbor] = candidate
                        heapq.heappush(queue, (candidate, neighbor))
            return result

        from_start = distances(0)
        from_end = distances(n - 1)
        shortest = from_start[-1]
        return [
            from_start[start] + weight + from_end[end] == shortest
            or from_start[end] + weight + from_end[start] == shortest
            for start, end, weight in edges
        ]


if __name__ == "__main__":
    test_cases = [
        (
            6,
            [[0, 1, 4], [0, 2, 1], [1, 3, 2], [2, 3, 1], [3, 4, 2], [4, 5, 1]],
            [False, True, False, True, True, True],
        )
    ]
    for _, (n, edges, expected) in enumerate(test_cases):
        assert Solution().findAnswer(n, edges) == expected
