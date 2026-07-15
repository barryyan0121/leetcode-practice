#
# @lc app=leetcode.cn id=732 lang=python3
#
# [732] 我的日程安排表 III
#

import os
import sys


# @lc code=start
class MyCalendarThree:
    def __init__(self):
        self.changes = {}

    def book(self, startTime: int, endTime: int) -> int:
        self.changes[startTime] = self.changes.get(startTime, 0) + 1
        self.changes[endTime] = self.changes.get(endTime, 0) - 1
        active = answer = 0
        for time in sorted(self.changes):
            active += self.changes[time]
            answer = max(answer, active)
        return answer


# @lc code=end


if __name__ == "__main__":
    obj = MyCalendarThree()
    test_cases = [
        (obj.book, (10, 20), 1),
        (obj.book, (50, 60), 1),
        (obj.book, (10, 40), 2),
        (obj.book, (5, 15), 3),
        (obj.book, (5, 10), 3),
        (obj.book, (25, 55), 3),
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
