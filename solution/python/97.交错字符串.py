#
# @lc app=leetcode.cn id=97 lang=python3
# @lcpr version=30202
#
# [97] 交错字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[n]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.isInterleave, ("aabcc", "dbbca", "aadbbcbcac"), True),
        (solution.isInterleave, ("aabcc", "dbbca", "aadbbbaccc"), False),
        (solution.isInterleave, ("", "", ""), True),
    ]

    for i, (func, args, want) in enumerate(test_cases):
        got = func(*args)
        assert got == want, (i, args, got, want)
