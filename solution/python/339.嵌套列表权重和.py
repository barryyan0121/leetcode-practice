#
# @lc app=leetcode.cn id=339 lang=python3
# @lcpr version=30203
#
# [339] 嵌套列表权重和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class NestedInteger:
    def __init__(self, value=None):
        self._value = value
        self._list = None if value is not None else []

    def isInteger(self):
        return self._list is None

    def add(self, elem):
        if self._list is None:
            self._list = []
            self._value = None
        self._list.append(elem)

    def setInteger(self, value):
        self._value = value
        self._list = None

    def getInteger(self):
        return self._value

    def getList(self):
        return self._list


# @lc code=start
class Solution:
    def depthSum(self, nestedList: List["NestedInteger"]) -> int:
        def dfs(items: List["NestedInteger"], depth: int) -> int:
            total = 0
            for ni in items:
                if ni.isInteger():
                    total += ni.getInteger() * depth
                else:
                    total += dfs(ni.getList() or [], depth + 1)
            return total

        return dfs(nestedList, 1)
        # @lc code=end


if __name__ == "__main__":
    def make_nested(value):
        if isinstance(value, int):
            return NestedInteger(value)
        ni = NestedInteger()
        for item in value:
            ni.add(make_nested(item))
        return ni

    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.depthSum, [[make_nested([1, 1]), make_nested(2), make_nested([1, 1])]], 10),
        (solution.depthSum, [[make_nested(1), make_nested([4, [6]])]], 27),
        (solution.depthSum, [[]], 0),
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

#
