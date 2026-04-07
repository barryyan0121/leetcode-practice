#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30203
#
# [283] 移动零
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert = 0
        for num in nums:
            if num != 0:
                nums[insert] = num
                insert += 1
        for i in range(insert, len(nums)):
            nums[i] = 0
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.moveZeroes, [[0, 1, 0, 3, 12]], [1, 3, 12, 0, 0]),
        (solution.moveZeroes, [[0]], [0]),
        (solution.moveZeroes, [[1, 2, 3]], [1, 2, 3]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            nums = args[0]
            func(*args)
            assert nums == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {nums}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {nums}"
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
# [0,1,0,3,12]\n
# @lcpr case=end

#
