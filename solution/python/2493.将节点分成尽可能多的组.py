"""2493. 将节点分成尽可能多的组"""


class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            first -= 1
            second -= 1
            graph[first].append(second)
            graph[second].append(first)
        color = [-1] * n
        answer = 0
        for start in range(n):
            if color[start] != -1:
                continue
            component = []
            queue = [start]
            color[start] = 0
            for node in queue:
                component.append(node)
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = color[node] ^ 1
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return -1
            groups = 0
            for source in component:
                distance = [-1] * n
                distance[source] = 1
                queue = [source]
                for node in queue:
                    for neighbor in graph[node]:
                        if distance[neighbor] == -1:
                            distance[neighbor] = distance[node] + 1
                            queue.append(neighbor)
                groups = max(groups, max(distance[node] for node in component))
            answer += groups
        return answer
