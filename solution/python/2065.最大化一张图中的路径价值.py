"""2065. 最大化一张图中的路径价值"""


class Solution:
    def maximalPathQuality(
        self, values: list[int], edges: list[list[int]], maxTime: int
    ) -> int:
        graph = [[] for _ in values]
        for x, y, time in edges:
            graph[x].append((y, time))
            graph[y].append((x, time))
        answer = values[0]
        visited = [0] * len(values)
        visited[0] = 1

        def search(node: int, time_left: int, score: int) -> None:
            nonlocal answer
            if node == 0:
                answer = max(answer, score)
            for neighbor, cost in graph[node]:
                if cost > time_left:
                    continue
                first = visited[neighbor] == 0
                visited[neighbor] += 1
                search(
                    neighbor,
                    time_left - cost,
                    score + (values[neighbor] if first else 0),
                )
                visited[neighbor] -= 1

        search(0, maxTime, values[0])
        return answer


if __name__ == "__main__":
    test_cases = [(([0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49), 75)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximalPathQuality(*args) == expected
