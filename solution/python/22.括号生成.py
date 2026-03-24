#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30202
#
# [22] 括号生成
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path: str, open_count: int, close_count: int) -> None:
            if len(path) == 2 * n:
                ans.append(path)
                return

            if open_count < n:
                backtrack(path + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(path + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.generateParenthesis,
            (3,),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        ),
        (solution.generateParenthesis, (1,), ["()"]),
        (solution.generateParenthesis, (2,), ["(())", "()()"]),
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
# 3\n
# @lcpr case=end

#
