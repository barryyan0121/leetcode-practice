# @lc app=leetcode.cn id=1453 lang=python3

from math import hypot, pi


class Solution:
    def numPoints(self, darts: list[list[int]], r: int) -> int:
        radius = float(r)
        candidates = [(x, y) for x, y in darts]
        for first in range(len(darts)):
            x1, y1 = darts[first]
            for second in range(first):
                x2, y2 = darts[second]
                distance = hypot(x2 - x1, y2 - y1)
                if distance > 2 * radius or distance == 0:
                    continue
                midpoint_x, midpoint_y = (x1 + x2) / 2, (y1 + y2) / 2
                height = (radius**2 - (distance / 2) ** 2) ** 0.5
                offset_x = -(y2 - y1) / distance * height
                offset_y = (x2 - x1) / distance * height
                candidates.extend(
                    [
                        (midpoint_x + offset_x, midpoint_y + offset_y),
                        (midpoint_x - offset_x, midpoint_y - offset_y),
                    ]
                )
        return max(
            sum((x - cx) ** 2 + (y - cy) ** 2 <= radius**2 + 1e-7 for x, y in darts)
            for cx, cy in candidates
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.numPoints, ([[-2, 0], [2, 0], [0, 2], [0, -2]], 2), 4)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1453 题 "圆形靶内的最大飞镖数量" 所有测试用例通过')
