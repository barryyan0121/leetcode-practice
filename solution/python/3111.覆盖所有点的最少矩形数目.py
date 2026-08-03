class Solution:
    def minRectanglesToCoverPoints(self, points: list[list[int]], w: int) -> int:
        x_coordinates = sorted(x for x, _ in points)
        answer = 0
        index = 0
        while index < len(x_coordinates):
            answer += 1
            right = x_coordinates[index] + w
            index += 1
            while index < len(x_coordinates) and x_coordinates[index] <= right:
                index += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        ([[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]], 1, 2),
        ([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]], 2, 3),
    ]
    for _, (points, w, expected) in enumerate(test_cases):
        assert Solution().minRectanglesToCoverPoints(points, w) == expected
