# @lc app=leetcode.cn id=1331 lang=python3

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {value: rank for rank, value in enumerate(sorted(set(arr)), 1)}
        return [ranks[value] for value in arr]


if __name__ == "__main__":
    test_cases = [
        (Solution().arrayRankTransform, ([40, 10, 20, 30],), [4, 1, 2, 3]),
        (Solution().arrayRankTransform, ([100, 100, 100],), [1, 1, 1]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1331 题 "数组序号转换" 所有测试用例通过')
