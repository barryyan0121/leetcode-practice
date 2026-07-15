#
# @lc app=leetcode.cn id=731 lang=python3
#
# [731] 我的日程安排表 II
#

import os
import sys


# @lc code=start
class MyCalendarTwo:
    def __init__(self):
        self.events = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        if any(startTime < end and start < endTime for start, end in self.overlaps):
            return False
        for start, end in self.events:
            if startTime < end and start < endTime:
                self.overlaps.append((max(startTime, start), min(endTime, end)))
        self.events.append((startTime, endTime))
        return True


# @lc code=end


if __name__ == "__main__":
    obj = MyCalendarTwo()
    test_cases = [
        (obj.book, (10, 20), True),
        (obj.book, (50, 60), True),
        (obj.book, (10, 40), True),
        (obj.book, (5, 15), False),
        (obj.book, (5, 10), True),
        (obj.book, (25, 55), True),
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
