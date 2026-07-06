#
# @lc app=leetcode.cn id=598 lang=python3
# @lcpr version=30203
#
# [598] 区间加法 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row, min_col = m, n
        for row, col in ops:
            min_row = min(min_row, row)
            min_col = min(min_col, col)
        return min_row * min_col


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxCount, (3, 3, [[2, 2], [3, 3]]), 4),
        (solution.maxCount, (3, 3, []), 9),
        (solution.maxCount, (18, 3, [[16, 1], [14, 3], [14, 2], [4, 1]]), 4),
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
# 3\n3\n[[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n[]\n
# @lcpr case=end

#
