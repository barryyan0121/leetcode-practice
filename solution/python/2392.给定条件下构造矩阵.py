"""2392. 给定条件下构造矩阵"""


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]
    ) -> list[list[int]]:
        def order(conditions: list[list[int]]) -> list[int] | None:
            graph = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)
            for before, after in conditions:
                graph[before].append(after)
                indegree[after] += 1
            queue = [node for node in range(1, k + 1) if indegree[node] == 0]
            result = []
            for node in queue:
                result.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            return result if len(result) == k else None

        rows, cols = order(rowConditions), order(colConditions)
        if rows is None or cols is None:
            return []
        row_index = {value: index for index, value in enumerate(rows)}
        col_index = {value: index for index, value in enumerate(cols)}
        answer = [[0] * k for _ in range(k)]
        for value in range(1, k + 1):
            answer[row_index[value]][col_index[value]] = value
        return answer
