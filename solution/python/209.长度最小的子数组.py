#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30202
#
# [209] 长度最小的子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        ans = float("inf")
        for right, num in enumerate(nums):
            total += num
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if ans == float("inf") else ans
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.minSubArrayLen, [7, [2, 3, 1, 2, 4, 3]], 2),
        (solution.minSubArrayLen, [4, [1, 4, 4]], 1),
        (solution.minSubArrayLen, [11, [1, 1, 1, 1, 1, 1, 1, 1]], 0),
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
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

#
