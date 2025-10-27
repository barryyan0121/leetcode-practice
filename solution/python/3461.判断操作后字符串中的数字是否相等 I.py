#
# @lc app=leetcode.cn id=3461 lang=python3
# @lcpr version=30300
#
# [3461] 判断操作后字符串中的数字是否相等 I
#

from itertools import pairwise
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(c) for c in s]
        while len(nums) > 2:
            nums = [(a + b) % 10 for a, b in pairwise(nums)]
        return nums[0] == nums[1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.hasSameDigits, ("3902",), True),
        (solution.hasSameDigits, ("34789",), False),
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
# "3902"\n
# @lcpr case=end

# @lcpr case=start
# "34789"\n
# @lcpr case=end

#
