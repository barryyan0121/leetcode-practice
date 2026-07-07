#
# @lc app=leetcode.cn id=619 lang=python3
# @lcpr version=30203
#
# [619] 只出现一次的最大数字
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def biggestSingleNumber(
        self, my_numbers: List[Dict[str, int]]
    ) -> List[Dict[str, Optional[int]]]:
        counts = Counter(row["num"] for row in my_numbers)
        singles = [num for num, count in counts.items() if count == 1]
        return [{"num": max(singles) if singles else None}]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.biggestSingleNumber,
            (
                [
                    {"num": 8},
                    {"num": 8},
                    {"num": 3},
                    {"num": 3},
                    {"num": 1},
                    {"num": 4},
                    {"num": 5},
                    {"num": 6},
                ],
            ),
            [{"num": 6}],
        ),
        (
            solution.biggestSingleNumber,
            ([{"num": 8}, {"num": 8}, {"num": 7}, {"num": 7}],),
            [{"num": None}],
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
