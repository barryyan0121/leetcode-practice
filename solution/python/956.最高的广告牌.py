#
# @lc app=leetcode.cn id=956 lang=python3
#
# [956] 最高的广告牌
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        heights = {0: 0}
        for rod in rods:
            updated = heights.copy()
            for difference, shorter in heights.items():
                updated[difference + rod] = max(
                    updated.get(difference + rod, 0), shorter
                )
                new_difference = abs(difference - rod)
                updated[new_difference] = max(
                    updated.get(new_difference, 0), shorter + min(difference, rod)
                )
            heights = updated
        return heights[0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.tallestBillboard, ([1, 2, 3, 6],), 6),
        (solution.tallestBillboard, ([1, 2, 3, 4, 5, 6],), 10),
        (solution.tallestBillboard, ([1, 2],), 0),
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
