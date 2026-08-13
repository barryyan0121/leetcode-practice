"""2473. 购买苹果的最低成本"""

from heapq import heappop, heappush


class Solution:
    def minCost(
        self, n: int, roads: list[list[int]], appleCost: list[int], k: int
    ) -> list[int]:
        graph = [[] for _ in range(n)]
        for start, end, cost in roads:
            weight = cost * (k + 1)
            graph[start - 1].append((end - 1, weight))
            graph[end - 1].append((start - 1, weight))
        answer = []
        for source in range(n):
            distance = [10**30] * n
            distance[source] = 0
            heap = [(0, source)]
            while heap:
                current, node = heappop(heap)
                if current != distance[node]:
                    continue
                for neighbor, weight in graph[node]:
                    candidate = current + weight
                    if candidate < distance[neighbor]:
                        distance[neighbor] = candidate
                        heappush(heap, (candidate, neighbor))
            answer.append(min(distance[index] + appleCost[index] for index in range(n)))
        return answer

if __name__ == "__main__":
    assert Solution().minCost(3, [[0,1,1],[1,2,1],[0,2,3]], [1,2,3], 1) == [1,2,3]
