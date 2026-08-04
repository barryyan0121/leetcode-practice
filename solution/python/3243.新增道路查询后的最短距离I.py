class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        graph = [[city + 1] if city + 1 < n else [] for city in range(n)]
        answer = []
        for start, end in queries:
            graph[start].append(end)
            distances = [-1] * n
            distances[0] = 0
            queue = [0]
            for city in queue:
                for neighbor in graph[city]:
                    if distances[neighbor] == -1:
                        distances[neighbor] = distances[city] + 1
                        queue.append(neighbor)
            answer.append(distances[-1])
        return answer


if __name__ == "__main__":
    test_cases = [
        ((5, [[2, 4], [0, 2], [0, 4]]), [3, 2, 1]),
        ((4, [[0, 3], [0, 2]]), [1, 1]),
    ]
    for _, ((n, queries), expected) in enumerate(test_cases):
        assert Solution().shortestDistanceAfterQueries(n, queries) == expected
