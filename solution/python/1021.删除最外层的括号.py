#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

import os
import sys


# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        result = []
        for parenthesis in s:
            if (parenthesis == "(" and depth) or (parenthesis == ")" and depth > 1):
                result.append(parenthesis)
            depth += 1 if parenthesis == "(" else -1
        return "".join(result)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.removeOuterParentheses, ("(()())(())",), "()()()"),
        (solution.removeOuterParentheses, ("(()())(())(()(()))",), "()()()()(())"),
        (solution.removeOuterParentheses, ("()()",), ""),
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
