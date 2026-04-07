#
# @lc app=leetcode.cn id=448 lang=python3
# @lcpr version=30203
#
# [448] 找到所有数组中消失的数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        return [i + 1 for i, num in enumerate(nums) if num > 0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findDisappearedNumbers, ([4, 3, 2, 7, 8, 2, 3, 1],), [5, 6]),
        (solution.findDisappearedNumbers, ([1, 1],), [2]),
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
# [4,3,2,7,8,2,3,1]\n
# @lcpr case=end
