#
# @lc app=leetcode.cn id=232 lang=python3
# @lcpr version=30203
#
# [232] 用栈实现队列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _move(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    def run_operations(ops: List[str], values: List[List[int]]) -> List[Optional[int]]:
        queue = None
        result = []
        for op, value in zip(ops, values):
            if op == "MyQueue":
                queue = MyQueue()
                result.append(None)
            elif op == "push":
                queue.push(value[0])
                result.append(None)
            elif op == "pop":
                result.append(queue.pop())
            elif op == "peek":
                result.append(queue.peek())
            elif op == "empty":
                result.append(queue.empty())
        return result

    test_cases = [
        (
            run_operations,
            (["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []]),
            [None, None, None, 1, 1, False],
        ),
        (
            run_operations,
            (["MyQueue", "push", "push", "push", "pop", "peek", "pop", "empty"], [[], [1], [2], [3], [], [], [], []]),
            [None, None, None, None, 1, 2, 2, False],
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
# ["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]\n
# @lcpr case=end
