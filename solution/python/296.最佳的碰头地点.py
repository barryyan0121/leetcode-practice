#
# @lc app=leetcode.cn id=296 lang=python3
# @lcpr version=30203
#
# [296] 最佳的碰头地点
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        rows.sort()
        cols.sort()

        def dist(arr: List[int]) -> int:
            i, j = 0, len(arr) - 1
            total = 0
            while i < j:
                total += arr[j] - arr[i]
                i += 1
                j -= 1
            return total

        return dist(rows) + dist(cols)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.minTotalDistance, [[[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]], 6),
        (solution.minTotalDistance, [[[1, 1]]], 1),
        (solution.minTotalDistance, [[[1]]], 0),
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
# [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]\n
# @lcpr case=end

#
