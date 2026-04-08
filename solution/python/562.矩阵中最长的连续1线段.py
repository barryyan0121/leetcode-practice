#
# @lc app=leetcode.cn id=562 lang=python3
# @lcpr version=30203
#
# [562] 矩阵中最长的连续1线段
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        horizontal = [0] * n
        vertical = [0] * n
        diag = [0] * n
        anti = [0] * n
        best = 0

        for i in range(m):
            new_diag = [0] * n
            new_anti = [0] * n
            for j in range(n):
                if mat[i][j] == 1:
                    horizontal[j] = horizontal[j - 1] + 1 if j > 0 else 1
                    vertical[j] += 1
                    new_diag[j] = diag[j - 1] + 1 if j > 0 else 1
                    new_anti[j] = anti[j + 1] + 1 if j + 1 < n else 1
                    best = max(
                        best,
                        horizontal[j],
                        vertical[j],
                        new_diag[j],
                        new_anti[j],
                    )
                else:
                    horizontal[j] = 0
                    vertical[j] = 0
            diag = new_diag
            anti = new_anti

        return best


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.longestLine, ([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]],), 3),
        (solution.longestLine, ([[1, 1, 1, 1]],), 4),
        (solution.longestLine, ([[0, 0], [0, 0]],), 0),
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
# [[0,1,1,0],[0,1,1,0],[0,0,0,1]]\n
# @lcpr case=end
#
