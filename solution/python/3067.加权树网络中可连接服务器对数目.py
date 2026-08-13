"""3067. 加权树网络中可连接服务器对数目"""


class Solution:
    def countPairsOfConnectableServers(
        self, edges: list[list[int]], signalSpeed: int
    ) -> list[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for a, b, weight in edges:
            graph[a].append((b, weight))
            graph[b].append((a, weight))

        def count_valid(node: int, parent: int, distance: int) -> int:
            total = 1 if distance % signalSpeed == 0 else 0
            for neighbor, weight in graph[node]:
                if neighbor != parent:
                    total += count_valid(neighbor, node, distance + weight)
            return total

        answer = [0] * n
        for center in range(n):
            prefix = 0
            for neighbor, weight in graph[center]:
                current = count_valid(neighbor, center, weight)
                answer[center] += prefix * current
                prefix += current
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], 1), [0, 4, 6, 6, 4, 0]),
        (
            (
                [
                    [0, 6, 3],
                    [6, 5, 3],
                    [0, 3, 1],
                    [3, 2, 7],
                    [3, 1, 6],
                    [3, 4, 2],
                ],
                3,
            ),
            [2, 0, 0, 0, 0, 0, 2],
        ),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countPairsOfConnectableServers(*args) == expected
