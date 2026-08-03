# @lc app=leetcode.cn id=1402 lang=python3
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        total = result = 0
        for value in sorted(satisfaction, reverse=True):
            total += value
            if total <= 0:
                break
            result += total
        return result


if __name__ == "__main__":
    test_cases = [
        (Solution().maxSatisfaction, ([-1, -8, 0, 5, -9],), 14),
        (Solution().maxSatisfaction, ([-1, -4, -5],), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1402 题 "做菜顺序" 所有测试用例通过')
