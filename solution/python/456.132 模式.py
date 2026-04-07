#
# @lc app=leetcode.cn id=456 lang=python3
# @lcpr version=30203
#
# [456] 132 模式
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float("-inf")
        for num in reversed(nums):
            if num < third:
                return True
            while stack and num > stack[-1]:
                third = stack.pop()
            stack.append(num)
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.find132pattern, ([1, 2, 3, 4],), False),
        (solution.find132pattern, ([3, 1, 4, 2],), True),
        (solution.find132pattern, ([-1, 3, 2, 0],), True),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

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
# [3,1,4,2]\n
# @lcpr case=end
