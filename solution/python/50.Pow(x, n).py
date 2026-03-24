#
# @lc app=leetcode.cn id=50 lang=python3
# @lcpr version=30202
#
# [50] Pow(x, n)
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        exponent = n
        base = x
        if exponent < 0:
            base = 1 / base
            exponent = -exponent

        result = 1.0
        while exponent > 0:
            if exponent & 1:
                result *= base
            base *= base
            exponent >>= 1
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.myPow, (2.0, 10), 1024.0),
        (solution.myPow, (2.1, 3), 9.261),
        (solution.myPow, (2.0, -2), 0.25),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert abs(result - expected) < 1e-9
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
# 2.00000\n10\n
# @lcpr case=end
