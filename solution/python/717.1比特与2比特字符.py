#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1 比特与 2 比特字符
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index = 0
        while index < len(bits) - 1:
            index += bits[index] + 1
        return index == len(bits) - 1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isOneBitCharacter, ([1, 0, 0],), True),
        (solution.isOneBitCharacter, ([1, 1, 1, 0],), False),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
