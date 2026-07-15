#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#

import os
import sys


# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        for index, character in enumerate(s):
            if character == "(":
                depth += 1
            else:
                depth -= 1
                if s[index - 1] == "(":
                    score += 1 << depth
        return score


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.scoreOfParentheses, ("()",), 1),
        (solution.scoreOfParentheses, ("(())",), 2),
        (solution.scoreOfParentheses, ("()()",), 2),
        (solution.scoreOfParentheses, ("(()(()))",), 6),
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
