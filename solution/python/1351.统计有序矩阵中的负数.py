# @lc app=leetcode.cn id=1351 lang=python3

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        column = len(grid[0]) - 1
        result = 0
        for row in grid:
            while column >= 0 and row[column] < 0:
                column -= 1
            result += len(row) - column - 1
        return result


if __name__ == "__main__":
    test_cases = [
        (
            Solution().countNegatives,
            ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],),
            8,
        ),
        (Solution().countNegatives, ([[3, 2], [1, 0]],), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1351 题 "统计有序矩阵中的负数" 所有测试用例通过')
