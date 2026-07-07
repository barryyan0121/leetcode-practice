#
# @lc app=leetcode.cn id=626 lang=python3
# @lcpr version=30203
#
# [626] 换座位
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def exchangeSeats(self, seat: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        students = {row["id"]: row["student"] for row in seat}
        n = len(seat)
        result = []
        for i in range(1, n + 1):
            if i % 2 == 1 and i < n:
                student = students[i + 1]
            elif i % 2 == 0:
                student = students[i - 1]
            else:
                student = students[i]
            result.append({"id": i, "student": student})
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.exchangeSeats,
            ([{"id": 1, "student": "Abbot"}, {"id": 2, "student": "Doris"}, {"id": 3, "student": "Emerson"}, {"id": 4, "student": "Green"}, {"id": 5, "student": "Jeames"}],),
            [{"id": 1, "student": "Doris"}, {"id": 2, "student": "Abbot"}, {"id": 3, "student": "Green"}, {"id": 4, "student": "Emerson"}, {"id": 5, "student": "Jeames"}],
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
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)

