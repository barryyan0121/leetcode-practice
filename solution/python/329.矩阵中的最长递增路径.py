#
# @lc app=leetcode.cn id=329 lang=python3
# @lcpr version=30203
#
# [329] 矩阵中的最长递增路径
#

import sys
import os
from functools import lru_cache

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            best = 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1 + dfs(ni, nj))
            return best

        return max(dfs(i, j) for i in range(m) for j in range(n))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.longestIncreasingPath, [[[9, 9, 4], [6, 6, 8], [2, 1, 1]]], 4),
        (solution.longestIncreasingPath, [[[3, 4, 5], [3, 2, 6], [2, 2, 1]]], 4),
        (solution.longestIncreasingPath, [[[1]]], 1),
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
# [[9,9,4],[6,6,8],[2,1,1]]\n
# @lcpr case=end

#
