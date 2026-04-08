#
# @lc app=leetcode.cn id=523 lang=python3
# @lcpr version=30203
#
# [523] 连续的子数组和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return any(a == b == 0 for a, b in zip(nums, nums[1:]))

        seen = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            mod = total % k
            if mod in seen:
                if i - seen[mod] > 1:
                    return True
            else:
                seen[mod] = i
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.checkSubarraySum, ([23, 2, 4, 6, 7], 6), True),
        (solution.checkSubarraySum, ([23, 2, 6, 4, 7], 13), False),
        (solution.checkSubarraySum, ([0, 0], 0), True),
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
# [23,2,4,6,7]\n6\n
# @lcpr case=end
#
