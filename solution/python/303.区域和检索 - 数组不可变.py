#
# @lc app=leetcode.cn id=303 lang=python3
# @lcpr version=30203
#
# [303] 区域和检索 - 数组不可变
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# @lc code=end


if __name__ == "__main__":

    def run_operations(ops: List[str], values: List[List[int]]) -> List[Optional[int]]:
        obj = None
        result = []

        for op, value in zip(ops, values):
            if op == "NumArray":
                obj = NumArray(value)
                result.append(None)
            else:
                result.append(obj.sumRange(*value))
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                ["NumArray", "sumRange", "sumRange", "sumRange"],
                [[-2, 0, 3, -5, 2, -1], [0, 2], [2, 5], [0, 5]],
            ),
            [None, 1, -1, -3],
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
# ["NumArray","sumRange","sumRange","sumRange"]\n[[-2,0,3,-5,2,-1],[0,2],[2,5],[0,5]]\n
# @lcpr case=end
