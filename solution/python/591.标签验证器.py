#
# @lc app=leetcode.cn id=591 lang=python3
# @lcpr version=30203
#
# [591] 标签验证器
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        n = len(code)

        while i < n:
            if i > 0 and not stack:
                return False

            if code.startswith("<![CDATA[", i):
                j = code.find("]]>", i + 9)
                if j == -1:
                    return False
                i = j + 3
            elif code.startswith("</", i):
                j = code.find(">", i + 2)
                if j == -1:
                    return False
                tag = code[i + 2 : j]
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
                i = j + 1
            elif code[i] == "<":
                j = code.find(">", i + 1)
                if j == -1:
                    return False
                tag = code[i + 1 : j]
                if not (1 <= len(tag) <= 9) or not tag.isalpha() or not tag.isupper():
                    return False
                stack.append(tag)
                i = j + 1
            else:
                i += 1

        return not stack


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.isValid,
            ("<DIV>This is the first line <![CDATA[<div>]]></DIV>",),
            True,
        ),
        (
            solution.isValid,
            ("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>",),
            True,
        ),
        (solution.isValid, ("<A>  <B> </A>   </B>",), False),
        (solution.isValid, ("<DIV>  div tag is not closed  <DIV>",), False),
        (solution.isValid, ("<DIV>  unmatched <  </DIV>",), False),
        (solution.isValid, ("<A<></A<>",), False),
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
# "<DIV>This is the first line <![CDATA[<div>]]></DIV>"\n
# @lcpr case=end

# @lcpr case=start
# "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"\n
# @lcpr case=end

# @lcpr case=start
# "<A>  <B> </A>   </B>"\n
# @lcpr case=end

#
