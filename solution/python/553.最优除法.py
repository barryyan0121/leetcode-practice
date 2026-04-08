#
# @lc app=leetcode.cn id=553 lang=python3
# @lcpr version=30203
#
# [553] 最优除法
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        return f"{nums[0]}/({'/'.join(map(str, nums[1:]))})"


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.optimalDivision, ([1000, 100, 10, 2],), "1000/(100/10/2)"),
        (solution.optimalDivision, ([2, 3, 4],), "2/(3/4)"),
        (solution.optimalDivision, ([2],), "2"),
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
# [1000,100,10,2]\n
# @lcpr case=end
#
