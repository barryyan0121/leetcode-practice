from collections import deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = [[] for _ in colors]
        indegree = [0] * len(colors)
        for source, target in edges:
            graph[source].append(target)
            indegree[target] += 1
        counts = [[0] * 26 for _ in colors]
        queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
        visited = 0
        answer = 0
        while queue:
            node = queue.popleft()
            visited += 1
            color = ord(colors[node]) - 97
            counts[node][color] += 1
            answer = max(answer, counts[node][color])
            for nxt in graph[node]:
                for index in range(26):
                    counts[nxt][index] = max(counts[nxt][index], counts[node][index])
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return answer if visited == len(colors) else -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3
    print("1857 passed")
