# @lc app=leetcode.cn id=1292 lang=python3

from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = (
                    mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
                )

        def valid(size: int) -> bool:
            for r in range(size, rows + 1):
                for c in range(size, cols + 1):
                    total = (
                        prefix[r][c]
                        - prefix[r - size][c]
                        - prefix[r][c - size]
                        + prefix[r - size][c - size]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right = 0, min(rows, cols)
        while left < right:
            mid = (left + right + 1) // 2
            if valid(mid):
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    test_cases = [
        (
            Solution().maxSideLength,
            ([[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4),
            2,
        ),
        (
            Solution().maxSideLength,
            (
                [
                    [2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2],
                ],
                1,
            ),
            0,
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1292 题 "元素和小于等于阈值的正方形的最大边长" 所有测试用例通过')
