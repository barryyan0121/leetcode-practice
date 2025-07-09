#
# @lc app=leetcode.cn id=738 lang=python3
# @lcpr version=30201
#
# [738] 单调递增的数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                # 向左回退处理连续相同字符 (如 332 → 299)
                while i > 0 and s[i] == s[i - 1]:
                    i -= 1
                s[i] = str(int(s[i]) - 1)
                s[i + 1 :] = "9" * (len(s) - i - 1)  # 后面全部置为9
                return int("".join(s))
        return int("".join(s))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    a = solution.monotoneIncreasingDigits(101)
    print(a)
    # your test code here


#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 1234\n
# @lcpr case=end

# @lcpr case=start
# 332\n
# @lcpr case=end

#
