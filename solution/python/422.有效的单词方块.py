#
# @lc app=leetcode.cn id=422 lang=python3
# @lcpr version=30203
#
# [422] 有效的单词方块
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for i in range(n):
            for j in range(len(words[i])):
                if j >= n or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.validWordSquare, [["abcd", "bnrt", "crmy", "dtye"]], True),
        (solution.validWordSquare, [["abcd", "bnrt", "crm", "dt"]], True),
        (solution.validWordSquare, [["ball", "area", "read", "lady"]], False),
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
# ["abcd","bnrt","crmy","dtye"]\n
# @lcpr case=end

#
