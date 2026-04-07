#
# @lc app=leetcode.cn id=213 lang=python3
# @lcpr version=30203
#
# [213] 打家劫舍 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(arr: List[int]) -> int:
            prev2 = prev1 = 0
            for num in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.rob, [[2, 3, 2]], 3),
        (solution.rob, [[1, 2, 3, 1]], 4),
        (solution.rob, [[1]], 1),
        (solution.rob, [[0]], 0),
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
# [2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

#
