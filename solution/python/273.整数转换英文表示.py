#
# @lc app=leetcode.cn id=273 lang=python3
# @lcpr version=30203
#
# [273] 整数转换英文表示
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        def helper(n: int) -> str:
            if n == 0:
                return ""
            if n < 20:
                return below_20[n]
            if n < 100:
                return tens[n // 10] + (" " + helper(n % 10) if n % 10 else "")
            if n < 1000:
                return (
                    below_20[n // 100]
                    + " Hundred"
                    + (" " + helper(n % 100) if n % 100 else "")
                )
            for value, word in [
                (10**9, "Billion"),
                (10**6, "Million"),
                (10**3, "Thousand"),
            ]:
                if n >= value:
                    return (
                        helper(n // value)
                        + " "
                        + word
                        + (" " + helper(n % value) if n % value else "")
                    )

        return helper(num)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.numberToWords, (123,), "One Hundred Twenty Three"),
        (
            solution.numberToWords,
            (12345,),
            "Twelve Thousand Three Hundred Forty Five",
        ),
        (
            solution.numberToWords,
            (1234567,),
            "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        ),
        (solution.numberToWords, (0,), "Zero"),
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
# 123\n
# @lcpr case=end
