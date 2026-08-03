# @lc app=leetcode.cn id=1296 lang=python3

from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        counts = Counter(nums)
        for value in sorted(counts):
            amount = counts[value]
            if amount:
                for next_value in range(value, value + k):
                    if counts[next_value] < amount:
                        return False
                    counts[next_value] -= amount
        return True


if __name__ == "__main__":
    test_cases = [
        (Solution().isPossibleDivide, ([1, 2, 3, 3, 4, 4, 5, 6], 4), True),
        (
            Solution().isPossibleDivide,
            ([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3),
            True,
        ),
        (Solution().isPossibleDivide, ([1, 2, 3, 4], 3), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1296 题 "划分数组为连续数字的集合" 所有测试用例通过')
