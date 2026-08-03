# @lc app=leetcode.cn id=1610 lang=python3


class Solution:
    def visiblePoints(
        self, points: list[list[int]], angle: int, location: list[int]
    ) -> int:
        import math

        same = sum(point == location for point in points)
        angles = sorted(
            math.degrees(math.atan2(y - location[1], x - location[0]))
            for x, y in points
            if [x, y] != location
        )
        extended = angles + [value + 360 for value in angles]
        answer = left = 0
        for right, value in enumerate(extended):
            while value - extended[left] > angle + 1e-10:
                left += 1
            answer = max(answer, right - left + 1)
        return same + answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.visiblePoints, ([[2, 1], [2, 2], [3, 3]], 90, [1, 1]), 3)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1610 题 "可见点的最大数目" 所有测试用例通过')
