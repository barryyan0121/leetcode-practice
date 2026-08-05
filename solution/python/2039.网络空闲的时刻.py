"""2039. 网络空闲的时刻"""

from collections import deque


class Solution:
    def networkBecomesIdle(self, edges: list[list[int]], patience: list[int]) -> int:
        graph = [[] for _ in patience]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        distance = [-1] * len(patience)
        distance[0] = 0
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distance[neighbor] < 0:
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
        answer = 0
        for node in range(1, len(patience)):
            round_trip = distance[node] * 2
            last_send = ((round_trip - 1) // patience[node]) * patience[node]
            answer = max(answer, last_send + round_trip)
        return answer + 1


if __name__ == "__main__":
    test_cases = [(([[0, 1], [1, 2]], [0, 2, 1]), 8)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().networkBecomesIdle(*args) == expected
