# @lc app=leetcode.cn id=1380 lang=python3
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        column_max = [max(column) for column in zip(*matrix)]
        return [value for row in matrix for value in [min(row)] if value in column_max]


if __name__ == "__main__":
    test_cases = [
        (Solution().luckyNumbers, ([[3, 7, 8], [9, 11, 13], [15, 16, 17]],), [15]),
        (
            Solution().luckyNumbers,
            ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]],),
            [12],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1380 题 "矩阵中的幸运数" 所有测试用例通过')
