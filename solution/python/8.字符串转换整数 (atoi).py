#
# @lc app=leetcode.cn id=8 lang=python3
# @lcpr version=30202
#
# [8] 字符串转换整数 (atoi)
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        # 记录正负号
        sign = 1
        # 用 long 避免 int 溢出
        res = 0
        # 跳过前导空格
        while i < n and s[i] == " ":
            i += 1
        if i == n:
            return 0

        # 记录符号位
        if i < n and s[i] == "-":
            sign = -1
            i += 1
        elif i < n and s[i] == "+":
            i += 1
        if i == n:
            return 0

        # 统计数字位
        while i < n and "0" <= s[i] <= "9":
            res = res * 10 + ord(s[i]) - ord("0")
            # 溢出判断
            if sign == 1 and res > 2**31 - 1:
                return 2**31 - 1
            if sign == -1 and res > 2**31:
                return -(2**31)
            i += 1

        # 如果溢出，强转成 int 就会和真实值不同
        return int(res) * sign
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.myAtoi, ("42",), 42),
        (solution.myAtoi, ("   -42",), -42),
        (solution.myAtoi, ("4193 with words",), 4193),
        (solution.myAtoi, ("   -042",), -42),
        (solution.myAtoi, ("1337c0d3",), 1337),
        (solution.myAtoi, ("0-1",), 0),
        (solution.myAtoi, ("words and 987",), 0),
        (solution.myAtoi, ("-91283472332",), -2147483648),
        (solution.myAtoi, ("91283472332",), 2147483647),
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
# "42"\n
# @lcpr case=end

# @lcpr case=start
# " -042"\n
# @lcpr case=end

# @lcpr case=start
# "1337c0d3"\n
# @lcpr case=end

# @lcpr case=start
# "0-1"\n
# @lcpr case=end

# @lcpr case=start
# "words and 987"\n
# @lcpr case=end

#
