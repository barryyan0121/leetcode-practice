"""2285. 道路的最大总重要性"""


class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        value = [0] * n
        for rank, node in enumerate(sorted(range(n), key=lambda i: degree[i]), 1):
            value[node] = rank
        return sum(value[a] + value[b] for a, b in roads)
