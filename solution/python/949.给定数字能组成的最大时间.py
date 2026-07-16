#
# @lc app=leetcode.cn id=949 lang=python3
#
# [949] 给定数字能组成的最大时间
#

import os
import sys
from itertools import permutations
from typing import List


# @lc code=start
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        valid = [
            digits
            for digits in permutations(arr)
            if digits[0] * 10 + digits[1] < 24 and digits[2] * 10 + digits[3] < 60
        ]
        if not valid:
            return ""
        hour1, hour2, minute1, minute2 = max(valid)
        return f"{hour1}{hour2}:{minute1}{minute2}"


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.largestTimeFromDigits, ([1, 2, 3, 4],), "23:41"),
        (solution.largestTimeFromDigits, ([5, 5, 5, 5],), ""),
        (solution.largestTimeFromDigits, ([0, 0, 1, 0],), "10:00"),
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
