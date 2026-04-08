#
# @lc app=leetcode.cn id=580 lang=python3
# @lcpr version=30203
#
# [580] 统计各专业学生人数
#

import sys
import os
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def countStudentNumber(
        self, student: List[Dict[str, Any]], department: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        counts: Dict[int, int] = defaultdict(int)
        for row in student:
            counts[row["dept_id"]] += 1

        result = []
        for row in department:
            result.append(
                {
                    "dept_name": row["dept_name"],
                    "student_number": counts[row["dept_id"]],
                }
            )

        result.sort(key=lambda row: (-row["student_number"], row["dept_name"]))
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.countStudentNumber,
            (
                [
                    {
                        "student_id": 1,
                        "student_name": "Jack",
                        "gender": "M",
                        "dept_id": 1,
                    },
                    {
                        "student_id": 2,
                        "student_name": "Jane",
                        "gender": "F",
                        "dept_id": 1,
                    },
                    {
                        "student_id": 3,
                        "student_name": "Mark",
                        "gender": "M",
                        "dept_id": 2,
                    },
                ],
                [
                    {"dept_id": 1, "dept_name": "Engineering"},
                    {"dept_id": 2, "dept_name": "Science"},
                    {"dept_id": 3, "dept_name": "Law"},
                ],
            ),
            [
                {"dept_name": "Engineering", "student_number": 2},
                {"dept_name": "Science", "student_number": 1},
                {"dept_name": "Law", "student_number": 0},
            ],
        ),
        (
            solution.countStudentNumber,
            (
                [
                    {"student_id": 1, "student_name": "A", "gender": "M", "dept_id": 2},
                    {"student_id": 2, "student_name": "B", "gender": "F", "dept_id": 1},
                ],
                [
                    {"dept_id": 1, "dept_name": "Alpha"},
                    {"dept_id": 2, "dept_name": "Beta"},
                    {"dept_id": 3, "dept_name": "Gamma"},
                ],
            ),
            [
                {"dept_name": "Alpha", "student_number": 1},
                {"dept_name": "Beta", "student_number": 1},
                {"dept_name": "Gamma", "student_number": 0},
            ],
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
