"""2360. 图中的最长环"""


class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        answer = -1
        visited = [False] * len(edges)
        for start in range(len(edges)):
            if visited[start]:
                continue
            depth = {}
            node, step = start, 0
            while node != -1 and not visited[node]:
                visited[node] = True
                depth[node] = step
                step += 1
                node = edges[node]
            if node in depth:
                answer = max(answer, step - depth[node])
        return answer


if __name__ == "__main__":
    assert Solution().longestCycle([3, 3, 4, 2, 3]) == 3
