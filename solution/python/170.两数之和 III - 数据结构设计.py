#
# @lc app=leetcode.cn id=170 lang=python3
# @lcpr version=30202
#
# [170] 两数之和 III - 数据结构设计
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import Counter
from common.node import *


# @lc code=start
class TwoSum:
    def __init__(self):
        self.count = Counter()

    def add(self, number: int) -> None:
        self.count[number] += 1

    def find(self, value: int) -> bool:
        for num, cnt in self.count.items():
            other = value - num
            if other == num:
                if cnt >= 2:
                    return True
            elif other in self.count:
                return True
        return False
        # @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    test_cases = [
        (
            [
                ("init", []),
                ("add", [1]),
                ("add", [3]),
                ("add", [5]),
                ("find", [4]),
                ("find", [7]),
            ],
            [None, None, None, None, True, False],
        ),
        (
            [
                ("init", []),
                ("add", [0]),
                ("add", [0]),
                ("find", [0]),
                ("find", [1]),
            ],
            [None, None, None, True, False],
        ),
    ]

    all_passed = True
    for idx, (ops, expected) in enumerate(test_cases):
        try:
            result = []
            obj = None
            for op, args in ops:
                if op == "init":
                    obj = TwoSum()
                    result.append(None)
                elif op == "add":
                    result.append(obj.add(*args))
                else:
                    result.append(obj.find(*args))
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {ops}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {ops}, 期望 = {expected}, 实际 = {result}"
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
# ["TwoSum","add","add","add","find","find"]\n[[],[1],[3],[5],[4],[7]]\n
# @lcpr case=end

#
