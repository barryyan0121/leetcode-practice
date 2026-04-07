#
# @lc app=leetcode.cn id=365 lang=python3
# @lcpr version=30203
#
# [365] 水壶问题
#

import sys
import os
from math import gcd

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def canMeasureWater(
        self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int
    ) -> bool:
        if targetCapacity == 0:
            return True
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug1Capacity == 0 or jug2Capacity == 0:
            return (
                targetCapacity == jug1Capacity
                or targetCapacity == jug2Capacity
                or targetCapacity == jug1Capacity + jug2Capacity
            )
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.canMeasureWater, [3, 5, 4], True),
        (solution.canMeasureWater, [2, 6, 5], False),
        (solution.canMeasureWater, [1, 2, 3], True),
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
# 3\n5\n4\n
# @lcpr case=end

#
