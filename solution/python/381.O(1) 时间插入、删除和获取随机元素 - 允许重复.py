#
# @lc app=leetcode.cn id=381 lang=python3
# @lcpr version=30203
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

import sys
import os
import random
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class RandomizedCollection:
    def __init__(self):
        self.values = []
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        existed = len(self.indices[val]) > 0
        self.values.append(val)
        self.indices[val].add(len(self.values) - 1)
        return not existed

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False

        remove_idx = self.indices[val].pop()
        last_val = self.values[-1]
        self.values[remove_idx] = last_val
        if remove_idx != len(self.values) - 1:
            self.indices[last_val].add(remove_idx)
            self.indices[last_val].discard(len(self.values) - 1)
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# @lc code=end


if __name__ == "__main__":

    def run_operations(ops: List[str], values: List[List[int]]) -> List[Any]:
        random.seed(0)
        obj = None
        result = []

        for op, value in zip(ops, values):
            if op == "RandomizedCollection":
                obj = RandomizedCollection()
                result.append(None)
            elif op == "insert":
                result.append(obj.insert(value[0]))
            elif op == "remove":
                result.append(obj.remove(value[0]))
            elif op == "getRandom":
                result.append(obj.getRandom())
        return result

    def check_result(result: List[Any], expected: List[Any]) -> bool:
        if len(result) != len(expected):
            return False
        for actual, target in zip(result, expected):
            if isinstance(target, set):
                if actual not in target:
                    return False
            elif actual != target:
                return False
        return True

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                [
                    "RandomizedCollection",
                    "insert",
                    "insert",
                    "insert",
                    "getRandom",
                    "remove",
                    "getRandom",
                ],
                [[], [1], [1], [2], [], [1], []],
            ),
            [None, True, False, True, {1, 2}, True, {1, 2}],
        ),
        (
            run_operations,
            (
                ["RandomizedCollection", "insert", "remove", "remove"],
                [[], [5], [5], [5]],
            ),
            [None, True, True, False],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert check_result(result, expected)
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
# ["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n[[],[1],[1],[2],[],[1],[]]\n
# @lcpr case=end
