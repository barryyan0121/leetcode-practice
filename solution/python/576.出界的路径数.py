#
# @lc app=leetcode.cn id=576 lang=python3
# @lcpr version=30203
#
# [576] 出界的路径数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        mod = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        ans = 0

        for _ in range(maxMove):
            next_dp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    ways = dp[r][c]
                    if not ways:
                        continue
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            next_dp[nr][nc] = (next_dp[nr][nc] + ways) % mod
                        else:
                            ans = (ans + ways) % mod
            dp = next_dp

        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findPaths, (2, 2, 2, 0, 0), 6),
        (solution.findPaths, (1, 3, 3, 0, 1), 12),
        (solution.findPaths, (3, 3, 1, 1, 1), 0),
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
