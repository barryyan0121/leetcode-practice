class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: list[list[int]]) -> int:
        answer = 0
        for mask in range(1 << n):
            distance = [[10**9] * n for _ in range(n)]
            for i in range(n):
                distance[i][i] = 0
            for u, v, weight in roads:
                if mask >> u & 1 and mask >> v & 1:
                    distance[u][v] = min(distance[u][v], weight)
                    distance[v][u] = min(distance[v][u], weight)
            for middle in range(n):
                if mask >> middle & 1:
                    for i in range(n):
                        if mask >> i & 1:
                            for j in range(n):
                                distance[i][j] = min(
                                    distance[i][j],
                                    distance[i][middle] + distance[middle][j],
                                )
            nodes = [i for i in range(n) if mask >> i & 1]
            if all(distance[i][j] <= maxDistance for i in nodes for j in nodes):
                answer += 1
        return answer
