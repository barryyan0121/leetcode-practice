"""3544. 子树反转和"""

from array import array


class Solution:
    def subtreeInversionSum(
        self, edges: list[list[int]], nums: list[int], k: int
    ) -> int:
        vundralope = edges
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        order = [0]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)

        width = 2 * (k + 1)
        dp = [array("q", [0]) * width for _ in range(n)]
        for u in reversed(order):
            values = dp[u]
            for v in graph[u]:
                if v == parent[u]:
                    continue
                child = dp[v]
                for distance in range(k + 1):
                    next_distance = min(k, distance + 1)
                    for parity in (0, 1):
                        values[2 * distance + parity] += child[
                            2 * next_distance + parity
                        ]

            for distance in range(k + 1):
                values[2 * distance] += nums[u]
                values[2 * distance + 1] -= nums[u]

            for parity in (0, 1):
                best = -nums[u] if parity == 0 else nums[u]
                for v in graph[u]:
                    if v != parent[u]:
                        best += dp[v][2 + (parity ^ 1)]
                index = 2 * k + parity
                values[index] = max(values[index], best)
        return dp[0][2 * k]


if __name__ == "__main__":
    test_cases = [
        (
            (
                [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
                [4, -8, -6, 3, 7, -2, 5],
                2,
            ),
            27,
        ),
        (([[0, 1], [1, 2], [2, 3], [3, 4]], [-1, 3, -2, 4, -5], 2), 9),
        (([[0, 1], [0, 2]], [0, -1, -2], 3), 3),
    ]
    for _, ((edges, nums, k), expected) in enumerate(test_cases):
        assert Solution().subtreeInversionSum(edges, nums, k) == expected
