#
# @lc app=leetcode.cn id=440 lang=python3
# @lcpr version=30203
#
# [440] 字典序的第K小数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(prefix: int) -> int:
            curr = prefix
            nxt = prefix + 1
            total = 0
            while curr <= n:
                total += min(n + 1, nxt) - curr
                curr *= 10
                nxt *= 10
            return total

        curr = 1
        k -= 1
        while k > 0:
            c = count(curr)
            if c <= k:
                k -= c
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findKthNumber, [13, 2], 10),
        (solution.findKthNumber, [1, 1], 1),
        (solution.findKthNumber, [100, 10], 17),
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
# 13\n2\n
# @lcpr case=end

#
