#
# @lc app=leetcode.cn id=544 lang=python3
# @lcpr version=30203
#
# [544] 输出比赛匹配对
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = [str(i) for i in range(1, n + 1)]
        while len(teams) > 1:
            teams = [f"({teams[i]},{teams[-1 - i]})" for i in range(len(teams) // 2)]
        return teams[0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findContestMatch, (2,), "(1,2)"),
        (solution.findContestMatch, (4,), "((1,4),(2,3))"),
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
# 4\n
# @lcpr case=end
#
