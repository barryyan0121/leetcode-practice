from math import hypot


class Solution:
    def getMinDistSum(self, positions: list[list[int]]) -> float:
        def distance(x: float, y: float) -> float:
            return sum(hypot(x - px, y - py) for px, py in positions)

        def best_y(x: float) -> float:
            low, high = 0.0, 100.0
            for _ in range(60):
                left = (2 * low + high) / 3
                right = (low + 2 * high) / 3
                if distance(x, left) < distance(x, right):
                    high = right
                else:
                    low = left
            return distance(x, (low + high) / 2)

        low, high = 0.0, 100.0
        for _ in range(60):
            left = (2 * low + high) / 3
            right = (low + 2 * high) / 3
            if best_y(left) < best_y(right):
                high = right
            else:
                low = left
        return best_y((low + high) / 2)


if __name__ == "__main__":
    test_cases = [
        ([[0, 1], [1, 0], [1, 2], [2, 1]], 4.0),
        ([[1, 1], [3, 3]], 2.8284271247461903),
    ]
    for _, (positions, expected) in enumerate(test_cases):
        assert abs(Solution().getMinDistSum(positions) - expected) < 1e-5
