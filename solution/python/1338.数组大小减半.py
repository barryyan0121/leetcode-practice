# @lc app=leetcode.cn id=1338 lang=python3

from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        removed = 0
        for count, frequency in enumerate(
            sorted(Counter(arr).values(), reverse=True), 1
        ):
            removed += frequency
            if removed * 2 >= len(arr):
                return count
        return 0


if __name__ == "__main__":
    test_cases = [
        (Solution().minSetSize, ([3, 3, 3, 3, 5, 5, 5, 2, 2, 7],), 2),
        (Solution().minSetSize, ([7, 7, 7, 7, 7, 7],), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1338 题 "数组大小减半" 所有测试用例通过')
