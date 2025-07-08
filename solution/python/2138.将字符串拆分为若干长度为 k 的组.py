#
# @lc app=leetcode.cn id=2138 lang=python3
# @lcpr version=30201
#
# [2138] 将字符串拆分为若干长度为 k 的组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        for i in range(0, n,  k):
            part = s[i:i + k]
            if len(part) < k:
                part += fill * (k - len(part))
            res.append(part)
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.divideString("abcdefghij", 3, "x"))
    # your test code here



#
# @lcpr case=start
# "abcdefghi"\n3\n"x"\n
# @lcpr case=end

# @lcpr case=start
# "abcdefghij"\n3\n"x"\n
# @lcpr case=end

#

