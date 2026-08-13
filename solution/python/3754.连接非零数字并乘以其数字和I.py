#
# @lc app=leetcode.cn id=3754 lang=python3
# @lcpr version=30203
#
# [3754] 连接非零数字并乘以其数字和 I
#

import os
import sys


# @lc code=start
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [int(ch) for ch in str(n) if ch != "0"]
        if not digits:
            return 0
        x = int("".join(map(str, digits)))
        return x * sum(digits)


# @lc code=end


if __name__ == "__main__":
    f = Solution().sumAndMultiply
    assert f(1234) == 12340
    assert f(10203004) == 12340
    assert f(1000) == 1
    assert f(0) == 0
