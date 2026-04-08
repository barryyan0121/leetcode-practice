#
# @lc app=leetcode.cn id=571 lang=python3
# @lcpr version=30203
#
# [571] 给定数字的频率查询中位数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findMedianGivenFrequencyOfNumbers(self, numbers: List[Dict[str, int]]) -> float:
        rows = sorted(numbers, key=lambda row: row["number"])
        total = sum(row["frequency"] for row in rows)

        def kth(k: int) -> int:
            running = 0
            for row in rows:
                running += row["frequency"]
                if running >= k:
                    return row["number"]
            raise ValueError("k is out of range")

        if total == 0:
            return 0.0
        if total % 2 == 1:
            return float(kth(total // 2 + 1))
        left = kth(total // 2)
        right = kth(total // 2 + 1)
        return (left + right) / 2


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findMedianGivenFrequencyOfNumbers,
            (
                [
                    {"number": 2, "frequency": 3},
                    {"number": 1, "frequency": 2},
                    {"number": 3, "frequency": 1},
                ],
            ),
            2.0,
        ),
        (
            solution.findMedianGivenFrequencyOfNumbers,
            (
                [
                    {"number": 1, "frequency": 1},
                    {"number": 2, "frequency": 1},
                    {"number": 10, "frequency": 2},
                ],
            ),
            6.0,
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert abs(result - expected) < 1e-9
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
# numbers = Numbers table\n
# @lcpr case=end
