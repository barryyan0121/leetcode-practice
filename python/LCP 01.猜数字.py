#
# @lc app=leetcode.cn id=LCP 01 lang=python3
# @lcpr version=30201
#
# [LCP 01] 猜数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(guess[i] == answer[i] for i in range(len(guess)))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,3]\n[3,2,1]\n
# @lcpr case=end

#
