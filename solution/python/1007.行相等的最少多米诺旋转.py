#
# @lc app=leetcode.cn id=1007 lang=python3
#
# [1007] 行相等的最少多米诺旋转
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def rotations(value):
            top = bottom = 0
            for first, second in zip(tops, bottoms):
                if first != value and second != value:
                    return float("inf")
                top += first != value
                bottom += second != value
            return min(top, bottom)

        result = min(rotations(tops[0]), rotations(bottoms[0]))
        return result if result != float("inf") else -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minDominoRotations, ([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]), 2),
        (solution.minDominoRotations, ([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]), -1),
        (solution.minDominoRotations, ([1, 1], [1, 1]), 0),
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
