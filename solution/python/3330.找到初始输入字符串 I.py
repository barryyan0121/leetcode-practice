#
# @lc app=leetcode.cn id=3330 lang=python3
# @lcpr version=30201
#
# [3330] 找到初始输入字符串 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
from collections import Counter

# @lc code=start
class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                res += 1
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# "abbcccc"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n
# @lcpr case=end

#
