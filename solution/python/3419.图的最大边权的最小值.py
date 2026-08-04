from collections import deque


class Solution:
    def minMaxWeight(self, n: int, edges: list[list[int]], threshold: int) -> int:
        if n == 1:
            return 0
        if threshold == 0:
            return -1
        reversed_edges = [[] for _ in range(n)]
        for source, target, weight in edges:
            reversed_edges[target].append((source, weight))
        weights = sorted({weight for _, _, weight in edges})

        def reachable(limit: int) -> bool:
            seen = [False] * n
            seen[0] = True
            queue = deque([0])
            count = 1
            while queue:
                node = queue.popleft()
                for previous, weight in reversed_edges[node]:
                    if weight <= limit and not seen[previous]:
                        seen[previous] = True
                        count += 1
                        queue.append(previous)
            return count == n

        if not weights or not reachable(weights[-1]):
            return -1
        left, right = 0, len(weights) - 1
        while left < right:
            middle = (left + right) // 2
            if reachable(weights[middle]):
                right = middle
            else:
                left = middle + 1
        return weights[left]


if __name__ == "__main__":
    test_cases = [
        ((5, [[1, 0, 1], [2, 0, 2], [3, 0, 1], [4, 3, 1], [2, 1, 1]], 2), 1),
        (
            (5, [[0, 1, 1], [0, 2, 2], [0, 3, 1], [0, 4, 1], [1, 2, 1], [1, 4, 1]], 1),
            -1,
        ),
        ((5, [[1, 2, 1], [1, 3, 3], [1, 4, 5], [2, 3, 2], [3, 4, 2], [4, 0, 1]], 1), 2),
    ]
    for _, ((n, edges, threshold), expected) in enumerate(test_cases):
        assert Solution().minMaxWeight(n, edges, threshold) == expected
