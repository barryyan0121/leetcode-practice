#
# @lc app=leetcode.cn id=446 lang=python3
# @lcpr version=30203
#
# [446] 等差数列划分 II - 子序列
#

import sys
import os
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in nums]
        total = 0

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j][diff]
                total += count
                dp[i][diff] += count + 1

        return total


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numberOfArithmeticSlices, ([2, 4, 6, 8, 10],), 7),
        (solution.numberOfArithmeticSlices, ([7, 7, 7, 7, 7],), 16),
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
# [2,4,6,8,10]\n
# @lcpr case=end
