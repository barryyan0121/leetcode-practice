#
# @lc app=leetcode.cn id=390 lang=python3
# @lcpr version=30203
#
# [390] 消除游戏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        left_to_right = True
        remaining = n

        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right

        return head


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.lastRemaining, (9,), 6),
        (solution.lastRemaining, (1,), 1),
        (solution.lastRemaining, (24,), 14),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# 9\n
# @lcpr case=end
