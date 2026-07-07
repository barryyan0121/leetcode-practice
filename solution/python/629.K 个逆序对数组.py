#
# @lc app=leetcode.cn id=629 lang=python3
# @lcpr version=30203
#
# [629] K 个逆序对数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * k
        for num in range(1, n + 1):
            new_dp = [0] * (k + 1)
            window = 0
            for inv in range(k + 1):
                window = (window + dp[inv]) % mod
                if inv >= num:
                    window = (window - dp[inv - num]) % mod
                new_dp[inv] = window
            dp = new_dp
        return dp[k]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.kInversePairs, (3, 0), 1),
        (solution.kInversePairs, (3, 1), 2),
        (solution.kInversePairs, (4, 2), 5),
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
