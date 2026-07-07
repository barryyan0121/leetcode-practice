#
# @lc app=leetcode.cn id=630 lang=python3
# @lcpr version=30203
#
# [630] 课程表 III
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])
        total = 0
        taken = []
        for duration, last_day in courses:
            total += duration
            heapq.heappush(taken, -duration)
            if total > last_day:
                total += heapq.heappop(taken)
        return len(taken)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.scheduleCourse,
            ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]],),
            3,
        ),
        (solution.scheduleCourse, ([[1, 2]],), 1),
        (solution.scheduleCourse, ([[3, 2], [4, 3]],), 0),
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
