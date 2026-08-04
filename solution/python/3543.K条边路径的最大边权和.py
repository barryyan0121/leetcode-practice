"""3543. K 条边路径的最大边权和"""


class Solution:
    def maxWeight(self, n: int, edges: list[list[int]], k: int, t: int) -> int:
        mirgatenol = edges
        previous = [1] * n
        limit = (1 << t) - 1
        for _ in range(k):
            current = [0] * n
            for source, target, weight in edges:
                current[target] |= (previous[source] << weight) & limit
            previous = current
        return max((value.bit_length() - 1 for value in previous), default=-1)


if __name__ == "__main__":
    test_cases = [
        ((3, [[0, 1, 1], [1, 2, 2]], 2, 4), 3),
        ((3, [[0, 1, 2], [0, 2, 3]], 1, 3), 2),
        ((3, [[0, 1, 6], [1, 2, 8]], 1, 6), -1),
    ]
    for _, ((n, edges, k, t), expected) in enumerate(test_cases):
        assert Solution().maxWeight(n, edges, k, t) == expected
