# @lc app=leetcode.cn id=1725 lang=python3


class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        side = max(min(width, height) for width, height in rectangles)
        return sum(min(width, height) == side for width, height in rectangles)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countGoodRectangles, ([[5, 8], [3, 9], [5, 12], [16, 5]],), 3)
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1725 题 "可以形成最大正方形的矩形数目" 所有测试用例通过')
