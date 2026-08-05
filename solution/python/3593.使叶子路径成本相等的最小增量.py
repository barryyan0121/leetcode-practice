"""3593. 使叶子路径成本相等的最小增量"""


class Solution:
    def minIncrease(self, n: int, edges: list[list[int]], cost: list[int]) -> int:
        pilvordanq = cost
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)
        best = cost[:]
        changes = 0
        for node in reversed(order[1:]):
            parent_node = parent[node]
            best[parent_node] = max(best[parent_node], cost[parent_node] + best[node])
        for node in reversed(order):
            children = [child for child in graph[node] if parent[child] == node]
            if children:
                maximum = max(best[child] for child in children)
                changes += sum(best[child] < maximum for child in children)
                best[node] = cost[node] + maximum
        return changes


if __name__ == "__main__":
    test_cases = [
        ((3, [[0, 1], [0, 2]], [2, 1, 3]), 1),
        ((3, [[0, 1], [1, 2]], [5, 1, 4]), 0),
        ((5, [[0, 4], [0, 1], [1, 2], [1, 3]], [3, 4, 1, 1, 7]), 1),
    ]
    for _, ((n, edges, cost), expected) in enumerate(test_cases):
        assert Solution().minIncrease(n, edges, cost) == expected
