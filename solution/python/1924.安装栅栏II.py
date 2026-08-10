"""1924. 安装栅栏 II"""

import random


class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[float]:
        points = [tuple(point) for point in trees]
        random.shuffle(points)

        def contains(
            circle: tuple[float, float, float], point: tuple[int, int]
        ) -> bool:
            x, y, radius = circle
            return (point[0] - x) ** 2 + (point[1] - y) ** 2 <= radius * radius + 1e-10

        def diameter(
            first: tuple[int, int], second: tuple[int, int]
        ) -> tuple[float, float, float]:
            x = (first[0] + second[0]) / 2
            y = (first[1] + second[1]) / 2
            return (
                x,
                y,
                ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** 0.5 / 2,
            )

        def circumcircle(first, second, third):
            determinant = 2 * (
                first[0] * (second[1] - third[1])
                + second[0] * (third[1] - first[1])
                + third[0] * (first[1] - second[1])
            )
            if abs(determinant) < 1e-12:
                candidates = [
                    diameter(first, second),
                    diameter(first, third),
                    diameter(second, third),
                ]
                return min(
                    (
                        circle
                        for circle in candidates
                        if all(
                            contains(circle, point) for point in (first, second, third)
                        )
                    ),
                    key=lambda circle: circle[2],
                )
            first_square = first[0] ** 2 + first[1] ** 2
            second_square = second[0] ** 2 + second[1] ** 2
            third_square = third[0] ** 2 + third[1] ** 2
            x = (
                first_square * (second[1] - third[1])
                + second_square * (third[1] - first[1])
                + third_square * (first[1] - second[1])
            ) / determinant
            y = (
                first_square * (third[0] - second[0])
                + second_square * (first[0] - third[0])
                + third_square * (second[0] - first[0])
            ) / determinant
            return x, y, ((first[0] - x) ** 2 + (first[1] - y) ** 2) ** 0.5

        circle = (float(points[0][0]), float(points[0][1]), 0.0)
        for i, point in enumerate(points):
            if contains(circle, point):
                continue
            circle = (float(point[0]), float(point[1]), 0.0)
            for j in range(i):
                if contains(circle, points[j]):
                    continue
                circle = diameter(point, points[j])
                for k in range(j):
                    if not contains(circle, points[k]):
                        circle = circumcircle(point, points[j], points[k])
        return list(circle)


if __name__ == "__main__":
    result = Solution().outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]])
    assert (
        abs(result[0] - 2) < 1e-5
        and abs(result[1] - 2) < 1e-5
        and abs(result[2] - 2) < 1e-5
    )
