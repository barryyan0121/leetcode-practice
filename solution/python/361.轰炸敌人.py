#
# @lc app=leetcode.cn id=361 lang=python3
# @lcpr version=30203
#
# [361] 轰炸敌人
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        row_hits = 0
        col_hits = [0] * n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == "W":
                    row_hits = 0
                    k = j
                    while k < n and grid[i][k] != "W":
                        if grid[i][k] == "E":
                            row_hits += 1
                        k += 1
                if i == 0 or grid[i - 1][j] == "W":
                    col_hits[j] = 0
                    k = i
                    while k < m and grid[k][j] != "W":
                        if grid[k][j] == "E":
                            col_hits[j] += 1
                        k += 1
                if grid[i][j] == "0":
                    ans = max(ans, row_hits + col_hits[j])
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.maxKilledEnemies,
            [[["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]],
            3,
        ),
        (solution.maxKilledEnemies, [[["W", "W"], ["W", "W"]]], 0),
        (solution.maxKilledEnemies, [[["0"]]], 0),
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
# [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]\n
# @lcpr case=end

#
