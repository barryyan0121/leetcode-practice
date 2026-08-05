"""2013. 检测正方形"""

from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: list[int]) -> None:
        self.points[point[0]][point[1]] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        answer = 0
        for other_x, ys in self.points.items():
            if other_x == x:
                continue
            side = other_x - x
            x_points = self.points.get(x, {})
            answer += ys[y] * (
                x_points.get(y - side, 0) * ys[y - side]
                + x_points.get(y + side, 0) * ys[y + side]
            )
        return answer


if __name__ == "__main__":
    test_cases = [([], 1)]
    for _, (args, expected) in enumerate(test_cases):
        squares = DetectSquares()
        for point in ([3, 10], [11, 2], [3, 2], [11, 10]):
            squares.add(point)
        assert squares.count([11, 10]) == expected
