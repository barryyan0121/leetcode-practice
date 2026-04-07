#
# @lc app=leetcode.cn id=341 lang=python3
# @lcpr version=30203
#
# [341] 扁平化嵌套列表迭代器
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        if isinstance(value, int):
            self.value = value
            self.children = None
        else:
            self.value = None
            self.children = value or []

    def isInteger(self):
        return self.value is not None

    def getInteger(self):
        return self.value

    def getList(self):
        return self.children


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            item = self.stack.pop().getList()
            self.stack.extend(item[::-1])
        return bool(self.stack)


# @lc code=end


if __name__ == "__main__":
    def build_nested(value):
        if isinstance(value, int):
            return NestedInteger(value)
        return NestedInteger([build_nested(item) for item in value])

    def run_iterator(data: List[Any]) -> List[int]:
        iterator = NestedIterator([build_nested(item) for item in data])
        result = []
        while iterator.hasNext():
            result.append(iterator.next())
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (run_iterator, ([[1, 1], 2, [1, 1]],), [1, 1, 2, 1, 1]),
        (run_iterator, ([1, [4, [6]]],), [1, 4, 6]),
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
# [[1,1],2,[1,1]]\n
# @lcpr case=end
