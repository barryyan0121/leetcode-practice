#
# @lc app=leetcode.cn id=346 lang=python3
# @lcpr version=30203
#
# [346] 数据流中的移动平均值
#

import sys
import os
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        return self.total / len(self.queue)


# @lc code=end


if __name__ == "__main__":
    def run_operations(ops: List[str], values: List[List[int]]) -> List[Optional[float]]:
        obj = None
        result = []

        for op, value in zip(ops, values):
            if op == "MovingAverage":
                obj = MovingAverage(value[0])
                result.append(None)
            else:
                result.append(obj.next(value[0]))
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                ["MovingAverage", "next", "next", "next", "next"],
                [[3], [1], [10], [3], [5]],
            ),
            [None, 1.0, 5.5, 4.666666666666667, 6.0],
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
# ["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]\n
# @lcpr case=end
