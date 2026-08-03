# @lc app=leetcode.cn id=1326 lang=python3

from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        furthest = [0] * (n + 1)
        for center, radius in enumerate(ranges):
            left, right = max(0, center - radius), min(n, center + radius)
            furthest[left] = max(furthest[left], right)
        taps = 0
        current_end = next_end = 0
        for position in range(n + 1):
            if position > next_end:
                return -1
            next_end = max(next_end, furthest[position])
            if position == current_end and position < n:
                taps += 1
                current_end = next_end
        return taps


if __name__ == "__main__":
    test_cases = [
        (Solution().minTaps, (5, [3, 4, 1, 1, 0, 0]), 1),
        (Solution().minTaps, (3, [0, 0, 0, 0]), -1),
        (Solution().minTaps, (7, [1, 2, 1, 0, 2, 1, 0, 1]), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1326 题 "灌溉花园的最少水龙头数目" 所有测试用例通过')
