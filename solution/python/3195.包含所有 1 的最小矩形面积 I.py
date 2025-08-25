#
# @lc app=leetcode.cn id=3195 lang=python3
# @lcpr version=30202
#
# [3195] 包含所有 1 的最小矩形面积 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        l = n
        r = 0
        u = m
        d = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                l = min(l, j)
                r = max(r, j)
                u = min(u, i)
                d = max(d, i)

        return (r - l + 1) * (d - u + 1)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.minimumArea, ([[0, 0, 1]],), 1),
        (solution.minimumArea, ([[0, 1, 0], [1, 0, 1]],), 6),
        (solution.minimumArea, ([[0, 0], [1, 0]],), 1),
        (solution.minimumArea, ([[1, 1], [1, 1]],), 4),
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
# [[0,1,0],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0],[1,0]]\n
# @lcpr case=end

#
