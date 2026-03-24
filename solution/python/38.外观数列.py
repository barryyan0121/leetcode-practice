#
# @lc app=leetcode.cn id=38 lang=python3
# @lcpr version=30202
#
# [38] 外观数列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"
        for _ in range(1, n):
            parts = []
            i = 0
            while i < len(current):
                j = i
                while j < len(current) and current[j] == current[i]:
                    j += 1
                parts.append(str(j - i))
                parts.append(current[i])
                i = j
            current = "".join(parts)
        return current


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.countAndSay, (1,), "1"),
        (solution.countAndSay, (4,), "1211"),
        (solution.countAndSay, (5,), "111221"),
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
# 4\n
# @lcpr case=end
