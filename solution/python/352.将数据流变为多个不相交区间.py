#
# @lc app=leetcode.cn id=352 lang=python3
# @lcpr version=30203
#
# [352] 将数据流变为多个不相交区间
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *
from bisect import bisect_left


# @lc code=start
class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        intervals = self.intervals
        i = bisect_left(intervals, [value, value])
        start = value
        end = value

        if i > 0 and intervals[i - 1][1] + 1 >= value:
            i -= 1
            start = intervals[i][0]
            end = max(end, intervals[i][1])
            intervals.pop(i)

        while i < len(intervals) and intervals[i][0] - 1 <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            intervals.pop(i)

        intervals.insert(i, [start, end])

    def getIntervals(self) -> List[List[int]]:
        return [interval[:] for interval in self.intervals]


# @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    def run_operations(ops: List[str], values: List[List[int]]) -> List[Any]:
        sr = None
        result = []
        for op, value in zip(ops, values):
            if op == "SummaryRanges":
                sr = SummaryRanges()
                result.append(None)
            elif op == "addNum":
                sr.addNum(value[0])
                result.append(None)
            elif op == "getIntervals":
                result.append(sr.getIntervals())
        return result

    test_cases = [
        (
            run_operations,
            (
                ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals"],
                [[], [1], [], [3], []],
            ),
            [None, None, [[1, 1]], None, [[1, 1], [3, 3]]],
        ),
        (
            run_operations,
            (
                ["SummaryRanges", "addNum", "addNum", "addNum", "getIntervals"],
                [[], [1], [2], [3], []],
            ),
            [None, None, None, None, [[1, 3]]],
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
# ["SummaryRanges","addNum","getIntervals"]\n[[],[1],[]]\n
# @lcpr case=end
