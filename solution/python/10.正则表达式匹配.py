#
# @lc app=leetcode.cn id=10 lang=python3
# @lcpr version=30202
#
# [10] 正则表达式匹配
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] in {".", s[i - 1]}:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] in {".", s[i - 1]}:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.isMatch, ("aa", "a"), False),
        (solution.isMatch, ("aa", "a*"), True),
        (solution.isMatch, ("ab", ".*"), True),
        (solution.isMatch, ("aab", "c*a*b"), True),
        (solution.isMatch, ("mississippi", "mis*is*p*."), False),
        (solution.isMatch, ("", "c*"), True),
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
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"a*"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n".*"\n
# @lcpr case=end

# @lcpr case=start
# "aab"\n"c*a*b"\n
# @lcpr case=end

#
