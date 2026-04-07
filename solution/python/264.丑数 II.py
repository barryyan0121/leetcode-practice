#
# @lc app=leetcode.cn id=264 lang=python3
# @lcpr version=30203
#
# [264] 丑数 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i2 = i3 = i5 = 0

        for i in range(1, n):
            next_num = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            ugly[i] = next_num
            if next_num == ugly[i2] * 2:
                i2 += 1
            if next_num == ugly[i3] * 3:
                i3 += 1
            if next_num == ugly[i5] * 5:
                i5 += 1

        return ugly[-1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.nthUglyNumber, (10,), 12),
        (solution.nthUglyNumber, (1,), 1),
        (solution.nthUglyNumber, (15,), 24),
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
# 10\n
# @lcpr case=end
