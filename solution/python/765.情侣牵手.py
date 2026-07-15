#
# @lc app=leetcode.cn id=765 lang=python3
#
# [765] 情侣牵手
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        positions = {person: index for index, person in enumerate(row)}
        swaps = 0
        for seat in range(0, len(row), 2):
            partner = row[seat] ^ 1
            if row[seat + 1] == partner:
                continue
            partner_seat = positions[partner]
            displaced = row[seat + 1]
            row[seat + 1], row[partner_seat] = row[partner_seat], row[seat + 1]
            positions[partner] = seat + 1
            positions[displaced] = partner_seat
            swaps += 1
        return swaps


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minSwapsCouples, ([0, 2, 1, 3],), 1),
        (solution.minSwapsCouples, ([3, 2, 0, 1],), 0),
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
