"""3588. 找到最大三角形面积"""

from collections import defaultdict


class Solution:
    def maxArea(self, coords: list[list[int]]) -> int:
        rows = defaultdict(lambda: [10**9, -(10**9)])
        columns = defaultdict(lambda: [10**9, -(10**9)])
        min_x = min(x for x, _ in coords)
        max_x = max(x for x, _ in coords)
        min_y = min(y for _, y in coords)
        max_y = max(y for _, y in coords)
        for x, y in coords:
            rows[y][0] = min(rows[y][0], x)
            rows[y][1] = max(rows[y][1], x)
            columns[x][0] = min(columns[x][0], y)
            columns[x][1] = max(columns[x][1], y)
        answer = 0
        for y, (left, right) in rows.items():
            answer = max(answer, (right - left) * max(y - min_y, max_y - y))
        for x, (bottom, top) in columns.items():
            answer = max(answer, (top - bottom) * max(x - min_x, max_x - x))
        return answer if answer else -1


if __name__ == "__main__":
    test_cases = [
        (([[1, 1], [1, 2], [3, 2], [3, 3]],), 2),
        (([[1, 1], [2, 2], [3, 3]],), -1),
    ]
    for _, ((coords,), expected) in enumerate(test_cases):
        assert Solution().maxArea(coords) == expected
