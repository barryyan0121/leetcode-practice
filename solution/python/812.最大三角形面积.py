#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#

import os
import sys
from itertools import combinations
from typing import List


# @lc code=start
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(
            abs(
                first[0] * (second[1] - third[1])
                + second[0] * (third[1] - first[1])
                + third[0] * (first[1] - second[1])
            )
            / 2
            for first, second, third in combinations(points, 3)
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.largestTriangleArea,
            ([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]],),
            2.0,
        ),
        (solution.largestTriangleArea, ([[1, 0], [0, 0], [0, 1]],), 0.5),
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
