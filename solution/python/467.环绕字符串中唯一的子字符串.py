#
# @lc app=leetcode.cn id=467 lang=python3
# @lcpr version=30203
#
# [467] 环绕字符串中唯一的子字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        best = [0] * 26
        cur = 0
        for i, ch in enumerate(p):
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:
                cur += 1
            else:
                cur = 1
            idx = ord(ch) - ord("a")
            best[idx] = max(best[idx], cur)
        return sum(best)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findSubstringInWraproundString, ["a"], 1),
        (solution.findSubstringInWraproundString, ["cac"], 2),
        (solution.findSubstringInWraproundString, ["zab"], 6),
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
# "zab"\n
# @lcpr case=end

#
