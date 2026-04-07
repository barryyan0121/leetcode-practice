#
# @lc app=leetcode.cn id=351 lang=python3
# @lcpr version=30203
#
# [351] 安卓系统手势解锁
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5
        skip[4][6] = skip[6][4] = 5
        skip[2][8] = skip[8][2] = 5

        visited = [False] * 10

        def dfs(cur: int, remain: int) -> int:
            if remain == 0:
                return 1
            visited[cur] = True
            total = 0
            for nxt in range(1, 10):
                mid = skip[cur][nxt]
                if not visited[nxt] and (mid == 0 or visited[mid]):
                    total += dfs(nxt, remain - 1)
            visited[cur] = False
            return total

        total = 0
        for length in range(m, n + 1):
            total += dfs(1, length - 1) * 4
            total += dfs(2, length - 1) * 4
            total += dfs(5, length - 1)
        return total


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.numberOfPatterns, (1, 1), 9),
        (solution.numberOfPatterns, (1, 2), 65),
        (solution.numberOfPatterns, (2, 2), 56),
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
# 1\n1\n
# @lcpr case=end
