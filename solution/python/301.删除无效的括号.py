#
# @lc app=leetcode.cn id=301 lang=python3
# @lcpr version=30203
#
# [301] 删除无效的括号
#

import sys
import os
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(expr: str) -> bool:
            balance = 0
            for ch in expr:
                if ch == "(":
                    balance += 1
                elif ch == ")":
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            current = queue.popleft()
            if is_valid(current):
                result.append(current)
                found = True
            if found:
                continue
            for i, ch in enumerate(current):
                if ch not in "()":
                    continue
                nxt = current[:i] + current[i + 1 :]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(words: List[str]) -> List[str]:
        return sorted(words)

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.removeInvalidParentheses, ("()())()",), ["(())()", "()()()"]),
        (solution.removeInvalidParentheses, ("(a)())()",), ["(a())()", "(a)()()"]),
        (solution.removeInvalidParentheses, (")(",), [""]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
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
# "()())()"\n
# @lcpr case=end
