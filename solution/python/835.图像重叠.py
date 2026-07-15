#
# @lc app=leetcode.cn id=835 lang=python3
#
# [835] 图像重叠
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        first = [
            (row, column)
            for row in range(len(img1))
            for column in range(len(img1))
            if img1[row][column]
        ]
        second = [
            (row, column)
            for row in range(len(img2))
            for column in range(len(img2))
            if img2[row][column]
        ]
        shifts = Counter(
            (row1 - row2, column1 - column2)
            for row1, column1 in first
            for row2, column2 in second
        )
        return max(shifts.values(), default=0)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.largestOverlap,
            ([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]),
            3,
        ),
        (solution.largestOverlap, ([[1]], [[1]]), 1),
        (solution.largestOverlap, ([[0]], [[0]]), 0),
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
