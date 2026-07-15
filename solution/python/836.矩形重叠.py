#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]) and max(
            rec1[1], rec2[1]
        ) < min(rec1[3], rec2[3])


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isRectangleOverlap, ([0, 0, 2, 2], [1, 1, 3, 3]), True),
        (solution.isRectangleOverlap, ([0, 0, 1, 1], [1, 0, 2, 1]), False),
        (solution.isRectangleOverlap, ([0, 0, 1, 1], [2, 2, 3, 3]), False),
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
