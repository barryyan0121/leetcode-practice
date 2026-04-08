#
# @lc app=leetcode.cn id=552 lang=python3
# @lcpr version=30203
#
# [552] 学生出勤记录 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        # dp[a][l] where a in {0,1}, l in {0,1,2}
        dp = [[0, 0, 0], [0, 0, 0]]
        dp[0][0] = 1
        for _ in range(n):
            ndp = [[0, 0, 0], [0, 0, 0]]
            for a in range(2):
                for l in range(3):
                    val = dp[a][l]
                    if not val:
                        continue
                    ndp[a][0] = (ndp[a][0] + val) % mod  # P
                    if a == 0:
                        ndp[1][0] = (ndp[1][0] + val) % mod  # A
                    if l < 2:
                        ndp[a][l + 1] = (ndp[a][l + 1] + val) % mod  # L
            dp = ndp
        return sum(sum(row) for row in dp) % mod


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.checkRecord, (1,), 3),
        (solution.checkRecord, (2,), 8),
        (solution.checkRecord, (3,), 19),
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
# 2\n
# @lcpr case=end
#
