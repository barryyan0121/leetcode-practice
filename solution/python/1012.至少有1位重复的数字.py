#
# @lc app=leetcode.cn id=1012 lang=python3
#
# [1012] 至少有 1 位重复的数字
#

import os
import sys
from math import perm


# @lc code=start
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = list(map(int, str(n + 1)))
        unique = sum(9 * perm(9, length - 1) for length in range(1, len(digits)))
        used = set()
        for index, digit in enumerate(digits):
            start = 1 if index == 0 else 0
            for candidate in range(start, digit):
                if candidate not in used:
                    unique += perm(9 - index, len(digits) - index - 1)
            if digit in used:
                break
            used.add(digit)
        return n - unique


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numDupDigitsAtMostN, (20,), 1),
        (solution.numDupDigitsAtMostN, (100,), 10),
        (solution.numDupDigitsAtMostN, (1000,), 262),
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
