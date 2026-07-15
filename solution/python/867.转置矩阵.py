#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(column) for column in zip(*matrix)]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.transpose,
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
        ),
        (solution.transpose, ([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]]),
        (solution.transpose, ([[1]],), [[1]]),
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
