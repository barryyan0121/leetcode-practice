"""2497. 图中最大星和"""


class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        neighbors = [[] for _ in vals]
        for first, second in edges:
            neighbors[first].append(vals[second])
            neighbors[second].append(vals[first])
        answer = max(vals)
        for node, values in enumerate(neighbors):
            values.sort(reverse=True)
            answer = max(
                answer, vals[node] + sum(value for value in values[:k] if value > 0)
            )
        return answer

if __name__ == "__main__":
    assert Solution().maxStarSum([1,2,3,4,10,-10,-20], [[0,1],[1,2],[1,3],[2,4],[2,5],[3,6]], 2) == 15
