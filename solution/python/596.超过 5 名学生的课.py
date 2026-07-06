#
# @lc app=leetcode.cn id=596 lang=python3
# @lcpr version=30203
#
# [596] 超过 5 名学生的课
#

import sys
import os
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findClasses(self, courses: List[Dict[str, str]]) -> List[str]:
        students_by_class: Dict[str, Set[str]] = defaultdict(set)
        for row in courses:
            students_by_class[row["class"]].add(row["student"])

        return sorted(
            class_name
            for class_name, students in students_by_class.items()
            if len(students) >= 5
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findClasses,
            (
                [
                    {"student": "A", "class": "Math"},
                    {"student": "B", "class": "English"},
                    {"student": "C", "class": "Math"},
                    {"student": "D", "class": "Biology"},
                    {"student": "E", "class": "Math"},
                    {"student": "F", "class": "Computer"},
                    {"student": "G", "class": "Math"},
                    {"student": "H", "class": "Math"},
                    {"student": "I", "class": "Math"},
                ],
            ),
            ["Math"],
        ),
        (solution.findClasses, ([{"student": "A", "class": "Math"}],), []),
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
# Courses table\n
# @lcpr case=end

