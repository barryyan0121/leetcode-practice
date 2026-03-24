#
# @lc app=leetcode.cn id=12 lang=python3
# @lcpr version=30202
#
# [12] 整数转罗马数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            1000,
            900,
            500,
            400,
            100,
            90,
            50,
            40,
            10,
            9,
            5,
            4,
            1,
        ]
        symbols = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        ans = []
        for value, symbol in zip(values, symbols):
            count, num = divmod(num, value)
            ans.append(symbol * count)
        return "".join(ans)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.intToRoman, (3,), "III"),
        (solution.intToRoman, (4,), "IV"),
        (solution.intToRoman, (9,), "IX"),
        (solution.intToRoman, (58,), "LVIII"),
        (solution.intToRoman, (1994,), "MCMXCIV"),
        (solution.intToRoman, (3999,), "MMMCMXCIX"),
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
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 9\n
# @lcpr case=end

# @lcpr case=start
# 58\n
# @lcpr case=end

# @lcpr case=start
# 1994\n
# @lcpr case=end

#
