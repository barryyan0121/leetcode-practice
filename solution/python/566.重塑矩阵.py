#
# @lc app=leetcode.cn id=566 lang=python3
# @lcpr version=30203
#
# [566] 重塑矩阵
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = [value for row in nums for value in row]
        if len(flat) != r * c:
            return nums
        return [flat[i : i + c] for i in range(0, len(flat), c)]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.matrixReshape,
            ([[1, 2], [3, 4]], 1, 4),
            [[1, 2, 3, 4]],
        ),
        (
            solution.matrixReshape,
            ([[1, 2], [3, 4]], 2, 4),
            [[1, 2], [3, 4]],
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


#
# @lcpr case=start
# nums = [[1,2],[3,4]], r = 1, c = 4\n
# @lcpr case=end
#
