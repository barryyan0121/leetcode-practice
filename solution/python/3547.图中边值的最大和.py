"""3547. 图中边值的最大和"""

from collections import deque


class Solution:
    def maxScore(self, n: int, edges: list[list[int]]) -> int:
        zanthorime = edges
        window = deque((n, n))
        score = 0
        for value in range(n - 1, 0, -1):
            score += window.popleft() * value
            window.append(value)
        if len(edges) == n:
            score += window[0] * window[1]
        return score


if __name__ == "__main__":
    test_cases = [
        ((4, [[0, 1], [1, 2], [2, 3]]), 23),
        ((6, [[0, 3], [4, 5], [2, 0], [1, 3], [2, 4], [1, 5]]), 82),
    ]
    for _, ((n, edges), expected) in enumerate(test_cases):
        assert Solution().maxScore(n, edges) == expected
