#
# @lc app=leetcode.cn id=1003 lang=python3
#
# [1003] 检查替换后的词是否有效
#

import os
import sys


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            stack.append(letter)
            if stack[-3:] == ["a", "b", "c"]:
                del stack[-3:]
        return not stack


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isValid, ("aabcbc",), True),
        (solution.isValid, ("abcabcababcc",), True),
        (solution.isValid, ("abccba",), False),
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
