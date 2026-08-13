class Solution:
    def maximumPoints(self, edges: list[list[int]], coins: list[int], k: int) -> int:
        n = len(coins)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int, parent: int, shift: int) -> int:
            value = coins[node] >> shift
            collect = value - k
            halve = value >> 1
            for child in graph[node]:
                if child != parent:
                    collect += dfs(child, node, shift)
                    halve += dfs(child, node, shift + 1)
            return max(collect, halve)

        return dfs(0, -1, 0)


if __name__ == "__main__":
    assert Solution().maximumPoints([[0, 1], [1, 2]], [1, 2, 3], 1) == 3
