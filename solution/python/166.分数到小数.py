#
# @lc app=leetcode.cn id=166 lang=python3
# @lcpr version=30203
#
# [166] 分数到小数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:

    def GCD(self, a: int, b: int) -> int:  # 求最大公约数
        c = a % b
        while c > 0:
            a, b = b, c
            c = a % b
        return b

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        D = 10  # 定义十进制
        sign = "-" * int(numerator / denominator < 0)  # 判断符号字符
        P = max(numerator, -numerator)
        Q = max(denominator, -denominator)
        m = self.GCD(P, Q)
        P, Q = P // m, Q // m  # 分子分母各取绝对值并约分
        if Q == 1:  # 若约分后分母为1，说明结果为整数，直接返回
            return sign + str(P)
        Int = str(P // Q)  # 整数部分子字符串
        P %= Q
        Float = ""
        m = self.GCD(Q, D)
        while (
            m > 1
        ):  # 小数的非循环部分开始，只要分母Q与10还有公约数，非循环部分就不结束
            P *= D // m
            Q //= m
            Float = Float + str(P // Q)
            P %= Q
            m = self.GCD(Q, D)
        if P == 0:  # 非循环部分结束，如果没有余数了，说明是有限小数，返回
            return sign + Int + "." + Float
        Loop = ""
        p0 = P  # 循环节开始，记住循环节起点的余数
        while 1:
            Loop = Loop + str((D * P) // Q)
            P = (D * P) % Q
            if P == p0:  # 循环过程中又一次遇到与起点相同的余数，循环终止
                break
        return sign + Int + "." + Float + "(" + Loop + ")"  # 返回整个字符串

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.fractionToDecimal, (1, 2), "0.5"),
        (solution.fractionToDecimal, (2, 1), "2"),
        (solution.fractionToDecimal, (4, 333), "0.(012)"),
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
# 1\n2\n
# @lcpr case=end

# @lcpr case=start
# 2\n1\n
# @lcpr case=end

# @lcpr case=start
# 4\n333\n
# @lcpr case=end

#
