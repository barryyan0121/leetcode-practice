#
# @lc app=leetcode.cn id=225 lang=python3
# @lcpr version=30203
#
# [225] 用队列实现栈
#

import sys
import os
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# @lc code=end


if __name__ == "__main__":
    def run_operations(ops: List[str], values: List[List[int]]) -> List[Optional[Union[int, bool]]]:
        stack = None
        result = []

        for op, value in zip(ops, values):
            if op == "MyStack":
                stack = MyStack()
                result.append(None)
            elif op == "push":
                stack.push(value[0])
                result.append(None)
            elif op == "pop":
                result.append(stack.pop())
            elif op == "top":
                result.append(stack.top())
            elif op == "empty":
                result.append(stack.empty())
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                ["MyStack", "push", "push", "top", "pop", "empty"],
                [[], [1], [2], [], [], []],
            ),
            [None, None, None, 2, 2, False],
        ),
        (
            run_operations,
            (
                ["MyStack", "push", "empty", "pop", "empty"],
                [[], [5], [], [], []],
            ),
            [None, None, False, 5, True],
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
# ["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]\n
# @lcpr case=end
