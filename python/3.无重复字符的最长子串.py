#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30201
#
# [3] 无重复字符的最长子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

