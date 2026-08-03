# @lc app=leetcode.cn id=1340 lang=python3

from functools import lru_cache
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @lru_cache(None)
        def reach(index: int) -> int:
            best = 1
            for step in range(1, d + 1):
                left = index - step
                if left < 0 or arr[left] >= arr[index]:
                    break
                best = max(best, 1 + reach(left))
            for step in range(1, d + 1):
                right = index + step
                if right >= len(arr) or arr[right] >= arr[index]:
                    break
                best = max(best, 1 + reach(right))
            return best

        return max(reach(index) for index in range(len(arr)))


if __name__ == "__main__":
    test_cases = [
        (Solution().maxJumps, ([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2), 4),
        (Solution().maxJumps, ([3, 3, 3, 3, 3], 3), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1340 题 "跳跃游戏 V" 所有测试用例通过')
