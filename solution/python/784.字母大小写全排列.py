#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = [""]
        for character in s:
            variants = (
                (character.lower(), character.upper())
                if character.isalpha()
                else (character,)
            )
            answer = [prefix + variant for prefix in answer for variant in variants]
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.letterCasePermutation, ("a1b2",), {"a1b2", "a1B2", "A1b2", "A1B2"}),
        (solution.letterCasePermutation, ("3z4",), {"3z4", "3Z4"}),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert set(result) == expected
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
