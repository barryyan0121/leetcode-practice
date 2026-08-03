# @lc app=leetcode.cn id=1386 lang=python3
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        blocked = {}
        for row, seat in reservedSeats:
            blocked[row] = blocked.get(row, 0) | 1 << (seat - 1)
        result = (n - len(blocked)) * 2
        left = sum(1 << i for i in range(1, 5))
        right = sum(1 << i for i in range(5, 9))
        middle = sum(1 << i for i in range(3, 7))
        for mask in blocked.values():
            groups = (not mask & left) + (not mask & right)
            if not groups and not mask & middle:
                groups = 1
            result += groups
        return result


if __name__ == "__main__":
    test_cases = [
        (
            Solution().maxNumberOfFamilies,
            (3, [[1, 2], [1, 3], [1, 8], [2, 6], [2, 7], [2, 8]]),
            4,
        ),
        (Solution().maxNumberOfFamilies, (2, [[1, 5], [1, 6], [1, 7], [1, 8]]), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1386 题 "安排电影院座位" 所有测试用例通过')
