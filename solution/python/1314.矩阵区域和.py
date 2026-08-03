# @lc app=leetcode.cn id=1314 lang=python3

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = (
                    mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
                )
        result = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                top, left = max(0, r - k), max(0, c - k)
                bottom, right = min(rows, r + k + 1), min(cols, c + k + 1)
                result[r][c] = (
                    prefix[bottom][right]
                    - prefix[top][right]
                    - prefix[bottom][left]
                    + prefix[top][left]
                )
        return result


if __name__ == "__main__":
    test_cases = [
        (
            Solution().matrixBlockSum,
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1),
            [[12, 21, 16], [27, 45, 33], [24, 39, 28]],
        ),
        (
            Solution().matrixBlockSum,
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2),
            [[45, 45, 45], [45, 45, 45], [45, 45, 45]],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1314 题 "矩阵区域和" 所有测试用例通过')
