# @lc app=leetcode.cn id=1401 lang=python3
class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        x = min(max(xCenter, x1), x2)
        y = min(max(yCenter, y1), y2)
        return (x - xCenter) ** 2 + (y - yCenter) ** 2 <= radius * radius


if __name__ == "__main__":
    test_cases = [
        (Solution().checkOverlap, (1, 0, 0, 1, -1, 3, 1), True),
        (Solution().checkOverlap, (1, 0, 0, 1, 1, 3, 3), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1401 题 "圆形和矩形是否有重叠" 所有测试用例通过')
