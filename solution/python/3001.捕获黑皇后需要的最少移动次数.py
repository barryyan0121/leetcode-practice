# @lc app=leetcode.cn id=3001 lang=python3


class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        rook_clear = True
        if a == e and c == a and min(b, f) < d < max(b, f):
            rook_clear = False
        if b == f and d == b and min(a, e) < c < max(a, e):
            rook_clear = False
        if rook_clear and (a == e or b == f):
            return 1

        bishop_clear = True
        if abs(c - e) == abs(d - f):
            if (
                abs(a - e) == abs(b - f)
                and abs(a - c) == abs(b - d)
                and min(c, e) < a < max(c, e)
            ):
                bishop_clear = False
            elif (
                abs(a - e) == abs(b - f)
                and abs(a - c) == abs(b - d)
                and min(d, f) < b < max(d, f)
            ):
                bishop_clear = False
        if bishop_clear and abs(c - e) == abs(d - f):
            return 1
        return 2


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minMovesToCaptureTheQueen, (1, 1, 3, 3, 1, 8), 1),
        (solution.minMovesToCaptureTheQueen, (1, 1, 3, 3, 8, 7), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 3001 题 "捕获黑皇后需要的最少移动次数" 所有测试用例通过')
