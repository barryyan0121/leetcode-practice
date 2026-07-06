#
# @lc app=leetcode.cn id=601 lang=python3
# @lcpr version=30203
#
# [601] 体育馆的人流量
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def humanTraffic(self, stadium: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        rows = sorted((row for row in stadium if row["people"] >= 100), key=lambda r: r["id"])
        valid_ids = set()
        start = 0
        for i, row in enumerate(rows):
            if i > 0 and row["id"] != rows[i - 1]["id"] + 1:
                if i - start >= 3:
                    valid_ids.update(r["id"] for r in rows[start:i])
                start = i
        if len(rows) - start >= 3:
            valid_ids.update(r["id"] for r in rows[start:])
        return [row for row in sorted(stadium, key=lambda r: r["id"]) if row["id"] in valid_ids]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.humanTraffic,
            (
                [
                    {"id": 1, "visit_date": "2017-01-01", "people": 10},
                    {"id": 2, "visit_date": "2017-01-02", "people": 109},
                    {"id": 3, "visit_date": "2017-01-03", "people": 150},
                    {"id": 4, "visit_date": "2017-01-04", "people": 99},
                    {"id": 5, "visit_date": "2017-01-05", "people": 145},
                    {"id": 6, "visit_date": "2017-01-06", "people": 1455},
                    {"id": 7, "visit_date": "2017-01-07", "people": 199},
                    {"id": 8, "visit_date": "2017-01-09", "people": 188},
                ],
            ),
            [
                {"id": 5, "visit_date": "2017-01-05", "people": 145},
                {"id": 6, "visit_date": "2017-01-06", "people": 1455},
                {"id": 7, "visit_date": "2017-01-07", "people": 199},
                {"id": 8, "visit_date": "2017-01-09", "people": 188},
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


#
# @lcpr case=start
# Stadium table\n
# @lcpr case=end

