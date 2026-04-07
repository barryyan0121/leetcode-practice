#
# @lc app=leetcode.cn id=423 lang=python3
# @lcpr version=30203
#
# [423] 从英文中重建数字
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        out = [0] * 10
        out[0] = cnt["z"]
        out[2] = cnt["w"]
        out[4] = cnt["u"]
        out[6] = cnt["x"]
        out[8] = cnt["g"]
        out[3] = cnt["h"] - out[8]
        out[5] = cnt["f"] - out[4]
        out[7] = cnt["s"] - out[6]
        out[1] = cnt["o"] - out[0] - out[2] - out[4]
        out[9] = cnt["i"] - out[5] - out[6] - out[8]
        return "".join(str(i) * out[i] for i in range(10))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.originalDigits, ["owoztneoer"], "012"),
        (solution.originalDigits, ["fviefuro"], "45"),
        (solution.originalDigits, ["zerozero"], "00"),
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
# "owoztneoer"\n
# @lcpr case=end

#
