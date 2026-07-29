from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(
            max(abs(x - a), abs(y - b)) for (a, b), (x, y) in zip(points, points[1:])
        )


if __name__ == "__main__":
    test_cases = [([[1, 1], [3, 4], [-1, 0]], 7), ([[3, 2], [-2, 2]], 5)]
    for _, (points, expected) in enumerate(test_cases):
        assert Solution().minTimeToVisitAllPoints(points) == expected
