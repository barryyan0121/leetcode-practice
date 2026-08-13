"""2492. 两个城市间路径的最小分数"""


class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for first, second, distance in roads:
            graph[first - 1].append((second - 1, distance))
            graph[second - 1].append((first - 1, distance))
        seen = {0}
        stack = [0]
        answer = 10**9
        while stack:
            node = stack.pop()
            for neighbor, distance in graph[node]:
                answer = min(answer, distance)
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return answer

if __name__ == "__main__":
    assert Solution().minScore(4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]) == 5
