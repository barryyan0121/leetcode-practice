#
# @lc app=leetcode.cn id=722 lang=python3
#
# [722] 删除注释
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        block = False
        current = []
        for line in source:
            index = 0
            while index < len(line):
                if block:
                    if line[index : index + 2] == "*/":
                        block = False
                        index += 2
                    else:
                        index += 1
                elif line[index : index + 2] == "/*":
                    block = True
                    index += 2
                elif line[index : index + 2] == "//":
                    break
                else:
                    current.append(line[index])
                    index += 1
            if current and not block:
                answer.append("".join(current))
                current = []
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.removeComments,
            (
                [
                    "/*Test program */",
                    "int main()",
                    "{ ",
                    "  // variable declaration ",
                    "int a, b, c;",
                    "/* This is a test",
                    "   multiline  ",
                    "   comment for ",
                    "   testing */",
                    "a = b + c;",
                    "}",
                ],
            ),
            ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"],
        ),
        (solution.removeComments, (["a/*comment", "line", "more_comment*/b"],), ["ab"]),
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
