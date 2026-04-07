#
# @lc app=leetcode.cn id=241 lang=python3
# @lcpr version=30203
#
# [241] 为运算表达式设计优先级
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from functools import lru_cache
from common.node import *


# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def dfs(expr: str) -> List[int]:
            res = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = dfs(expr[:i])
                    right = dfs(expr[i + 1 :])
                    for a in left:
                        for b in right:
                            if ch == "+":
                                res.append(a + b)
                            elif ch == "-":
                                res.append(a - b)
                            else:
                                res.append(a * b)
            if not res:
                res.append(int(expr))
            return res

        return dfs(expression)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.diffWaysToCompute, ["2-1-1"], [0, 2]),
        (solution.diffWaysToCompute, ["2*3-4*5"], [-34, -14, -10, -10, 10]),
        (solution.diffWaysToCompute, ["10"], [10]),
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
# "2-1-1"\n
# @lcpr case=end

#
