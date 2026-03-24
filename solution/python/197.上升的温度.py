#
# @lc app=leetcode.cn id=197 lang=python3
# @lcpr version=30203
#
# [197] 上升的温度
#

import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def risingTemperature(self, weather: List[Dict[str, Union[int, str]]]) -> List[int]:
        by_date = {row["recordDate"]: row for row in weather}
        result = []

        for row in weather:
            current_date = datetime.strptime(row["recordDate"], "%Y-%m-%d").date()
            prev_date = (current_date - timedelta(days=1)).isoformat()
            if prev_date in by_date and row["temperature"] > by_date[prev_date]["temperature"]:
                result.append(row["id"])

        return sorted(result)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.risingTemperature,
            (
                [
                    {"id": 1, "recordDate": "2015-01-01", "temperature": 10},
                    {"id": 2, "recordDate": "2015-01-02", "temperature": 25},
                    {"id": 3, "recordDate": "2015-01-03", "temperature": 20},
                    {"id": 4, "recordDate": "2015-01-04", "temperature": 30},
                ],
            ),
            [2, 4],
        ),
        (
            solution.risingTemperature,
            (
                [
                    {"id": 1, "recordDate": "2024-01-01", "temperature": 5},
                    {"id": 2, "recordDate": "2024-01-03", "temperature": 8},
                ],
            ),
            [],
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
# weather = Weather table\n
# @lcpr case=end
