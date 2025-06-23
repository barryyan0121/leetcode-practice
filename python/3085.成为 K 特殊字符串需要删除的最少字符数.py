#
# @lc app=leetcode.cn id=3085 lang=python3
# @lcpr version=30201
#
# [3085] 成为 K 特殊字符串需要删除的最少字符数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1
        res = len(word)
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            res = min(res, deleted)
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "aabcaba"\n0\n
# @lcpr case=end

# @lcpr case=start
# "dabdcbdcdcd"\n2\n
# @lcpr case=end

# @lcpr case=start
# "aaabaaa"\n2\n
# @lcpr case=end

#

