#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30203
#
# [155] 最小栈
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# @lc code=end


if __name__ == "__main__":

    def run_operations(ops: List[str], values: List[List[int]]) -> List[Optional[int]]:
        stack = None
        result = []

        for op, value in zip(ops, values):
            if op == "MinStack":
                stack = MinStack()
                result.append(None)
            elif op == "push":
                stack.push(value[0])
                result.append(None)
            elif op == "pop":
                stack.pop()
                result.append(None)
            elif op == "top":
                result.append(stack.top())
            elif op == "getMin":
                result.append(stack.getMin())
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
                [[], [-2], [0], [-3], [], [], [], []],
            ),
            [None, None, None, None, -3, None, 0, -2],
        ),
        (
            run_operations,
            (
                ["MinStack", "push", "push", "getMin", "top", "pop", "getMin"],
                [[], [2], [1], [], [], [], []],
            ),
            [None, None, None, 1, 1, None, 2],
        ),
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
# ["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end
