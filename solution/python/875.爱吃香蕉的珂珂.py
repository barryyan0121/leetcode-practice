#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            speed = (left + right) // 2
            hours = sum((pile + speed - 1) // speed for pile in piles)
            if hours <= h:
                right = speed
            else:
                left = speed + 1
        return left


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minEatingSpeed, ([3, 6, 7, 11], 8), 4),
        (solution.minEatingSpeed, ([30, 11, 23, 4, 20], 5), 30),
        (solution.minEatingSpeed, ([30, 11, 23, 4, 20], 6), 23),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
