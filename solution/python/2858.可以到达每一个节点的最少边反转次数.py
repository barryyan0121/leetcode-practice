"""2858. 可以到达每一个节点的最少边反转次数"""


class Solution:
    def minEdgeReversals(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]
        for source, target in edges:
            graph[source].append((target, 0))
            graph[target].append((source, 1))
        answer = [0] * n

        def first(node: int, parent: int) -> int:
            total = 0
            for neighbor, cost in graph[node]:
                if neighbor != parent:
                    total += cost + first(neighbor, node)
            return total

        answer[0] = first(0, -1)

        def second(node: int, parent: int) -> None:
            for neighbor, cost in graph[node]:
                if neighbor != parent:
                    answer[neighbor] = answer[node] + (1 if cost == 0 else -1)
                    second(neighbor, node)

        second(0, -1)
        return answer


if __name__ == "__main__":
    test_cases = [((4, [[0, 1], [2, 0], [3, 2]]), [2, 3, 1, 2])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minEdgeReversals(*args) == expected
