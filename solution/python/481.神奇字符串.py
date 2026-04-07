#
# @lc app=leetcode.cn id=481 lang=python3
# @lcpr version=30203
#
# [481] 神奇字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        s = [1, 2, 2]
        i = 2
        num = 1
        while len(s) < n:
            s.extend([num] * s[i])
            num = 3 - num
            i += 1
        return s[:n].count(1)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.magicalString, (1,), 1),
        (solution.magicalString, (6,), 3),
        (solution.magicalString, (10,), 5),
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
# 6\n
# @lcpr case=end

#
