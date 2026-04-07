#
# @lc app=leetcode.cn id=307 lang=python3
# @lcpr version=30203
#
# [307] 区域和检索 - 数组可修改
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.bit = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, index: int, delta: int) -> None:
        while index < len(self.bit):
            self.bit[index] += delta
            index += index & -index

    def _query(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.bit[index]
            index -= index & -index
        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right + 1) - self._query(left)


# @lc code=end


if __name__ == "__main__":
    def run_operations(ops: List[str], values: List[List[int]]) -> List[Optional[int]]:
        obj = None
        result = []

        for op, value in zip(ops, values):
            if op == "NumArray":
                obj = NumArray(value)
                result.append(None)
            elif op == "update":
                obj.update(*value)
                result.append(None)
            else:
                result.append(obj.sumRange(*value))
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                ["NumArray", "sumRange", "update", "sumRange"],
                [[1, 3, 5], [0, 2], [1, 2], [0, 2]],
            ),
            [None, 9, None, 8],
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
# ["NumArray","sumRange","update","sumRange"]\n[[1,3,5],[0,2],[1,2],[0,2]]\n
# @lcpr case=end
