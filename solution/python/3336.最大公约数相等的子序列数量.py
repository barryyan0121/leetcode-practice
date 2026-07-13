#
# @lc app=leetcode.cn id=3336 lang=python3
#
# [3336] 最大公约数相等的子序列数量
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *
from collections import defaultdict
from math import gcd


# @lc code=start
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        dp = {(0, 0): 1}

        for num in nums:
            next_dp = defaultdict(int, dp)
            for (gcd1, gcd2), count in dp.items():
                next_dp[gcd(gcd1, num), gcd2] += count
                next_dp[gcd1, gcd(gcd2, num)] += count
            dp = {state: count % mod for state, count in next_dp.items()}

        return (
            sum(count for (gcd1, gcd2), count in dp.items() if gcd1 == gcd2 > 0) % mod
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.subsequencePairCount, ([1, 2, 3, 4],), 10),
        (solution.subsequencePairCount, ([10, 20, 30],), 2),
        (solution.subsequencePairCount, ([1, 1, 1, 1],), 50),
        (solution.subsequencePairCount, ([1],), 0),
        (solution.subsequencePairCount, ([1, 1],), 2),
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
