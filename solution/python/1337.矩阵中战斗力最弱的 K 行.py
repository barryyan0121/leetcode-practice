# @lc app=leetcode.cn id=1337 lang=python3

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [
            index
            for _, index in sorted((sum(row), index) for index, row in enumerate(mat))[
                :k
            ]
        ]


if __name__ == "__main__":
    test_cases = [
        (
            Solution().kWeakestRows,
            (
                [
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1],
                ],
                3,
            ),
            [2, 0, 3],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1337 题 "矩阵中战斗力最弱的 K 行" 所有测试用例通过')
