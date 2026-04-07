#
# @lc app=leetcode.cn id=294 lang=python3
# @lcpr version=30203
#
# [294] 翻转游戏 II
#

import sys
import os
from functools import lru_cache

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def canWin(self, currentState: str) -> bool:
        @lru_cache(None)
        def dfs(state: str) -> bool:
            chars = list(state)
            for i in range(len(chars) - 1):
                if chars[i] == "+" and chars[i + 1] == "+":
                    nxt = state[:i] + "--" + state[i + 2 :]
                    if not dfs(nxt):
                        return True
            return False

        return dfs(currentState)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.canWin, ["++++"], True),
        (solution.canWin, ["+"], False),
        (solution.canWin, ["+++"], True),
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
# "++++"\n
# @lcpr case=end

#
