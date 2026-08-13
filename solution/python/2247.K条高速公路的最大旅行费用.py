"""2247. K 条高速公路的最大旅行费用"""


class Solution:
    def maximumCost(self, n: int, highways: list[list[int]], k: int) -> int:
        graph = [[] for _ in range(n)]
        for a, b, toll in highways:
            graph[a].append((b, toll))
            graph[b].append((a, toll))
        dp = [[-1] * n for _ in range(1 << n)]
        for node in range(n):
            dp[1 << node][node] = 0
        for mask in range(1 << n):
            if mask.bit_count() >= k + 1:
                continue
            for node in range(n):
                if dp[mask][node] < 0:
                    continue
                for neighbor, toll in graph[node]:
                    if mask >> neighbor & 1 == 0:
                        new_mask = mask | (1 << neighbor)
                        dp[new_mask][neighbor] = max(
                            dp[new_mask][neighbor], dp[mask][node] + toll
                        )
        answer = -1
        for mask in range(1 << n):
            if mask.bit_count() == k + 1:
                answer = max(answer, max(dp[mask]))
        return answer

if __name__ == "__main__":
    assert Solution().maximumCost(4, [[0,1,5],[1,2,10],[2,3,2],[0,3,20]], 2) == 25
