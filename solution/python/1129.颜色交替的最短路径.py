from collections import deque


class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        graph = [[[] for _ in range(n)] for _ in range(2)]
        for color, edges in enumerate((redEdges, blueEdges)):
            for start, end in edges:
                graph[color][start].append(end)
        answer = [-1] * n
        queue = deque([(0, 0, 0), (0, 1, 0)])
        seen = {(0, 0), (0, 1)}
        while queue:
            node, color, distance = queue.popleft()
            if answer[node] == -1:
                answer[node] = distance
            for nxt in graph[color][node]:
                state = (nxt, 1 - color)
                if state not in seen:
                    seen.add(state)
                    queue.append((nxt, 1 - color, distance + 1))
        return answer


if __name__ == "__main__":
    test_cases = [
        (3, [[0, 1], [1, 2]], [], [0, 1, -1]),
        (3, [[0, 1]], [[1, 2]], [0, 1, 2]),
    ]
    for _, (n, red, blue, expected) in enumerate(test_cases):
        assert Solution().shortestAlternatingPaths(n, red, blue) == expected
