# @lc app=leetcode.cn id=1403 lang=python3
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        chosen = []
        current = 0
        for value in sorted(nums, reverse=True):
            chosen.append(value)
            current += value
            if current > total - current:
                break
        return chosen


if __name__ == "__main__":
    test_cases = [
        (Solution().minSubsequence, ([4, 3, 10, 9, 8],), [10, 9]),
        (Solution().minSubsequence, ([4, 4, 7, 6, 7],), [7, 7, 6]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1403 题 "非递增顺序的最小子序列" 所有测试用例通过')
