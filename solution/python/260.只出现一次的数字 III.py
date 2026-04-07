#
# @lc app=leetcode.cn id=260 lang=python3
# @lcpr version=30203
#
# [260] 只出现一次的数字 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        diff = xor & -xor
        a = b = 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        return [a, b]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.singleNumber, [[1, 2, 1, 3, 2, 5]], [3, 5]),
        (solution.singleNumber, [[-1, 0]], [-1, 0]),
        (solution.singleNumber, [[0, 1]], [0, 1]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = sorted(func(*args))
            assert result == sorted(expected)
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
# [1,2,1,3,2,5]\n
# @lcpr case=end

#
