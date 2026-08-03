# @lc app=leetcode.cn id=1375 lang=python3

from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        result = maximum = 0
        for position, bulb in enumerate(flips, 1):
            maximum = max(maximum, bulb)
            result += maximum == position
        return result


if __name__ == "__main__":
    test_cases = [
        (Solution().numTimesAllBlue, ([2, 1, 3, 5, 4],), 3),
        (Solution().numTimesAllBlue, ([3, 2, 4, 1, 5],), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1375 题 "灯泡开关 III" 所有测试用例通过')
