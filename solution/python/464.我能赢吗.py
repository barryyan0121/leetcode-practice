#
# @lc app=leetcode.cn id=464 lang=python3
# @lcpr version=30203
#
# [464] 我能赢吗
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from functools import lru_cache
from common.node import *


# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        total = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if total < desiredTotal:
            return False

        @lru_cache(None)
        def dfs(used: int, remain: int) -> bool:
            for num in range(1, maxChoosableInteger + 1):
                bit = 1 << (num - 1)
                if used & bit:
                    continue
                if num >= remain or not dfs(used | bit, remain - num):
                    return True
            return False

        return dfs(0, desiredTotal)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.canIWin, [10, 11], False),
        (solution.canIWin, [10, 0], True),
        (solution.canIWin, [5, 50], False),
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
# 10\n11\n
# @lcpr case=end

#
