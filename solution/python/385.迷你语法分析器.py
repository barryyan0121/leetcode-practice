#
# @lc app=leetcode.cn id=385 lang=python3
# @lcpr version=30203
#
# [385] 迷你语法分析器
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self.value = None
            self.children = []
        else:
            self.value = value
            self.children = None

    def isInteger(self):
        return self.children is None

    def add(self, elem):
        self.children.append(elem)

    def setInteger(self, value):
        self.value = value
        self.children = None

    def getInteger(self):
        return self.value

    def getList(self):
        return self.children


# @lc code=start
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":
            return NestedInteger(int(s))

        stack = []
        number = ""
        for char in s:
            if char == "[":
                stack.append(NestedInteger())
            elif char == "]":
                if number:
                    stack[-1].add(NestedInteger(int(number)))
                    number = ""
                item = stack.pop()
                if stack:
                    stack[-1].add(item)
                else:
                    return item
            elif char == ",":
                if number:
                    stack[-1].add(NestedInteger(int(number)))
                    number = ""
            else:
                number += char

        return NestedInteger()


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def serialize(item: NestedInteger):
        if item.isInteger():
            return item.getInteger()
        return [serialize(child) for child in item.getList()]

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.deserialize, ("324",), 324),
        (solution.deserialize, ("[123,[456,[789]]]",), [123, [456, [789]]]),
        (solution.deserialize, ("[-1,[2,-3]]",), [-1, [2, -3]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = serialize(func(*args))
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
# "[123,[456,[789]]]"\n
# @lcpr case=end
