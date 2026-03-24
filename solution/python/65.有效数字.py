#
# @lc app=leetcode.cn id=65 lang=python3
# @lcpr version=30202
#
# [65] 有效数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        seen_num = False
        seen_dot = False
        seen_exp = False
        seen_num_after_exp = True

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_num = True
                if seen_exp:
                    seen_num_after_exp = True
            elif ch in "+-":
                if i != 0 and s[i - 1].lower() != "e":
                    return False
            elif ch == ".":
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif ch.lower() == "e":
                if seen_exp or not seen_num:
                    return False
                seen_exp = True
                seen_num_after_exp = False
            else:
                return False

        return seen_num and seen_num_after_exp


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.isNumber, ("0",), True),
        (solution.isNumber, ("e",), False),
        (solution.isNumber, ("2e10",), True),
        (solution.isNumber, (" -90e3   ",), True),
        (solution.isNumber, (" 1e",), False),
        (solution.isNumber, ("1a",), False),
        (solution.isNumber, ("53.5e93",), True),
        (solution.isNumber, ("--6",), False),
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
# "0"\n
# @lcpr case=end

# @lcpr case=start
# "2e10"\n
# @lcpr case=end
