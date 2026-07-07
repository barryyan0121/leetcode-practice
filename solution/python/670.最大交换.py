#
# @lc app=leetcode.cn id=670 lang=python3
# @lcpr version=30203
#
# [670] 最大交换
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(ch): i for i, ch in enumerate(digits)}
        for i, ch in enumerate(digits):
            cur = int(ch)
            for d in range(9, cur, -1):
                if last.get(d, -1) > i:
                    j = last[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maximumSwap, (2736,), 7236),
        (solution.maximumSwap, (9973,), 9973),
        (solution.maximumSwap, (98368,), 98863),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)

