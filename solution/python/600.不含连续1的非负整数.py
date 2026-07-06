#
# @lc app=leetcode.cn id=600 lang=python3
# @lcpr version=30203
#
# [600] 不含连续1的非负整数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:
        fib = [0] * 32
        fib[0] = 1
        fib[1] = 2
        for i in range(2, 32):
            fib[i] = fib[i - 1] + fib[i - 2]

        ans = 0
        prev_bit = 0
        for bit in range(30, -1, -1):
            if n & (1 << bit):
                ans += fib[bit]
                if prev_bit:
                    return ans
                prev_bit = 1
            else:
                prev_bit = 0

        return ans + 1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findIntegers, (5,), 5),
        (solution.findIntegers, (1,), 2),
        (solution.findIntegers, (2,), 3),
        (solution.findIntegers, (100,), 34),
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
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#
