# @lc app=leetcode.cn id=1427 lang=python3

from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        offset = sum(amount if direction else -amount for direction, amount in shift)
        offset %= len(s)
        return s[-offset:] + s[:-offset] if offset else s


if __name__ == "__main__":
    test_cases = [
        (Solution().stringShift, ("abc", [[0, 1], [1, 2]]), "cab"),
        (
            Solution().stringShift,
            ("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]),
            "efgabcd",
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1427 题 "字符串的左右移" 所有测试用例通过')
