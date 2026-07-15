#
# @lc app=leetcode.cn id=699 lang=python3
#
# [699] 掉落的方块
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals = []
        answer = []
        highest = 0
        for left, size in positions:
            right = left + size
            base = max(
                (
                    height
                    for start, end, height in intervals
                    if left < end and start < right
                ),
                default=0,
            )
            height = base + size
            intervals.append((left, right, height))
            highest = max(highest, height)
            answer.append(highest)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.fallingSquares, ([[1, 2], [2, 3], [6, 1]],), [2, 5, 5]),
        (solution.fallingSquares, ([[100, 100], [200, 100]],), [100, 100]),
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
