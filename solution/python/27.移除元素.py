#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_list = [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
        ([1], 1, 0, []),
        ([4, 5], 3, 2, [4, 5]),
    ]
    test_cases = []
    for nums, val, expected_len, expected_nums in test_list:
        test_cases.append(
            (solution.removeElement, (nums, val), (expected_len, expected_nums))
        )

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            nums = args[0]
            result = func(*args)
            assert result == expected[0]
            assert nums[:result] == expected[1]
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
# [3,2,2,3]\n3\n
# @lcpr case=end

#
