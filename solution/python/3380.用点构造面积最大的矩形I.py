from itertools import combinations


class Solution:
    def maxRectangleArea(self, points: list[list[int]]) -> int:
        point_set = {tuple(point) for point in points}
        answer = -1
        x_values = sorted({x for x, _ in points})
        y_values = sorted({y for _, y in points})
        for left, right in combinations(x_values, 2):
            for bottom, top in combinations(y_values, 2):
                corners = {
                    (left, bottom),
                    (left, top),
                    (right, bottom),
                    (right, top),
                }
                if not corners <= point_set:
                    continue
                if any(
                    left <= x <= right and bottom <= y <= top and (x, y) not in corners
                    for x, y in points
                ):
                    continue
                answer = max(answer, (right - left) * (top - bottom))
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[1, 1], [1, 3], [3, 1], [3, 3]],), 4),
        (([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]],), -1),
        (([[1, 1], [1, 3], [3, 1], [3, 3], [1, 2], [3, 2]],), 2),
    ]
    for _, ((points,), expected) in enumerate(test_cases):
        assert Solution().maxRectangleArea(points) == expected
