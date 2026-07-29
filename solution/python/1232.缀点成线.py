from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        dx, dy = coordinates[1][0] - x0, coordinates[1][1] - y0
        return all((x - x0) * dy == (y - y0) * dx for x, y in coordinates[2:])


if __name__ == "__main__":
    test_cases = [
        ([[1, 2], [2, 3], [3, 4]], True),
        ([[1, 1], [2, 2], [3, 4]], False),
    ]
    for _, (coordinates, expected) in enumerate(test_cases):
        assert Solution().checkStraightLine(coordinates) == expected
