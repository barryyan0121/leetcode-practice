#
# @lc app=leetcode.cn id=3304 lang=python3
# @lcpr version=30201
#
# [3304] 找出第 K 个字符 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def kthCharacter(self, k: int) -> str:
        letters = ["a"]
        while len(letters) < k:
            n = len(letters)
            for i in range(n):
                letters.append(chr(ord(letters[i]) + 1))

        return letters[k - 1]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    solution.kthCharacter(5)
    # your test code here


#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#
