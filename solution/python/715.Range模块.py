#
# @lc app=leetcode.cn id=715 lang=python3
#
# [715] Range 模块
#

import os
import sys
from bisect import bisect_left, bisect_right


# @lc code=start
class RangeModule:
    def __init__(self):
        self.points = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect_left(self.points, left)
        end = bisect_right(self.points, right)
        middle = ([left] if start % 2 == 0 else []) + ([right] if end % 2 == 0 else [])
        self.points[start:end] = middle

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect_right(self.points, left)
        end = bisect_left(self.points, right)
        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect_left(self.points, left)
        end = bisect_right(self.points, right)
        middle = ([left] if start % 2 == 1 else []) + ([right] if end % 2 == 1 else [])
        self.points[start:end] = middle


# @lc code=end


if __name__ == "__main__":
    obj = RangeModule()
    obj.addRange(10, 20)
    obj.removeRange(14, 16)
    test_cases = [
        (obj.queryRange, (10, 14), True),
        (obj.queryRange, (13, 15), False),
        (obj.queryRange, (16, 17), True),
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
