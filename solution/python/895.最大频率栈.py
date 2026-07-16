#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

import os
import sys
from collections import defaultdict


# @lc code=start
class FreqStack:
    def __init__(self):
        self.frequency = defaultdict(int)
        self.groups = defaultdict(list)
        self.maximum = 0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        frequency = self.frequency[val]
        self.maximum = max(self.maximum, frequency)
        self.groups[frequency].append(val)

    def pop(self) -> int:
        value = self.groups[self.maximum].pop()
        self.frequency[value] -= 1
        if not self.groups[self.maximum]:
            self.maximum -= 1
        return value


# @lc code=end


def run_operations(operations):
    stack = FreqStack()
    result = []
    for operation, value in operations:
        if operation == "push":
            stack.push(value)
        else:
            result.append(stack.pop())
    return result


if __name__ == "__main__":
    test_cases = [
        (
            run_operations,
            (
                [
                    ("push", 5),
                    ("push", 7),
                    ("push", 5),
                    ("push", 7),
                    ("push", 4),
                    ("push", 5),
                    ("pop", None),
                    ("pop", None),
                    ("pop", None),
                    ("pop", None),
                ],
            ),
            [5, 7, 5, 4],
        ),
        (
            run_operations,
            ([("push", 1), ("push", 1), ("pop", None), ("pop", None)],),
            [1, 1],
        ),
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
