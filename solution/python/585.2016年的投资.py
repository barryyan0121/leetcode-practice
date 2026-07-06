#
# @lc app=leetcode.cn id=585 lang=python3
# @lcpr version=30203
#
# [585] 2016年的投资
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findInvestments(self, insurance: List[Dict[str, Any]]) -> float:
        tiv_2015_count = Counter(row["tiv_2015"] for row in insurance)
        location_count = Counter((row["lat"], row["lon"]) for row in insurance)
        total = sum(
            row["tiv_2016"]
            for row in insurance
            if tiv_2015_count[row["tiv_2015"]] > 1
            and location_count[(row["lat"], row["lon"])] == 1
        )
        return round(total + 1e-9, 2)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findInvestments,
            (
                [
                    {"pid": 1, "tiv_2015": 10, "tiv_2016": 5, "lat": 10, "lon": 10},
                    {"pid": 2, "tiv_2015": 20, "tiv_2016": 20, "lat": 20, "lon": 20},
                    {"pid": 3, "tiv_2015": 10, "tiv_2016": 30, "lat": 20, "lon": 20},
                    {"pid": 4, "tiv_2015": 10, "tiv_2016": 40, "lat": 40, "lon": 40},
                ],
            ),
            45.0,
        ),
        (
            solution.findInvestments,
            (
                [
                    {"pid": 1, "tiv_2015": 1, "tiv_2016": 2, "lat": 1, "lon": 1},
                    {"pid": 2, "tiv_2015": 2, "tiv_2016": 3, "lat": 2, "lon": 2},
                ],
            ),
            0.0,
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
# Insurance table\n
# @lcpr case=end

