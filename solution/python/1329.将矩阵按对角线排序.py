# @lc app=leetcode.cn id=1329 lang=python3

from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        for row in range(len(mat)):
            for column in range(len(mat[0])):
                diagonals[row - column].append(mat[row][column])
        for values in diagonals.values():
            values.sort(reverse=True)
        for row in range(len(mat)):
            for column in range(len(mat[0])):
                mat[row][column] = diagonals[row - column].pop()
        return mat


if __name__ == "__main__":
    test_cases = [
        (
            Solution().diagonalSort,
            ([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]],),
            [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1329 题 "将矩阵按对角线排序" 所有测试用例通过')
