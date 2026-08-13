class Solution:
    def placedCoins(self, edges: list[list[int]], cost: list[int]) -> list[int]:
        n = len(cost)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        answer = [1] * n

        def dfs(node: int, parent: int) -> list[int]:
            values = [cost[node]]
            for child in graph[node]:
                if child != parent:
                    values.extend(dfs(child, node))
            values.sort()
            if len(values) >= 3:
                answer[node] = max(
                    0,
                    values[-1] * values[-2] * values[-3],
                    values[0] * values[1] * values[-1],
                )
            return values if len(values) <= 6 else values[:3] + values[-3:]

        dfs(0, -1)
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.placedCoins(
        [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]], [1, 2, 3, 4, 5, 6]
    ) == [120, 1, 1, 1, 1, 1]
    assert solution.placedCoins([[0, 1], [0, 2]], [1, 2, -2]) == [0, 1, 1]
