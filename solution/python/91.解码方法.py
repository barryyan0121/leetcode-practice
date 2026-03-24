#
# @lc app=leetcode.cn id=91 lang=python3
# @lcpr version=30202
#
# [91] 解码方法
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        prev2 = 1
        prev1 = 1
        for i in range(1, len(s)):
            curr = 0
            if s[i] != "0":
                curr += prev1

            two = int(s[i - 1 : i + 1])
            if 10 <= two <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.numDecodings, ["12"], 2),
        (solution.numDecodings, ["226"], 3),
        (solution.numDecodings, ["06"], 0),
        (solution.numDecodings, ["11106"], 2),
        (solution.numDecodings, ["2101"], 1),
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
# "12"\n
# @lcpr case=end

# @lcpr case=start
# "226"\n
# @lcpr case=end

#
