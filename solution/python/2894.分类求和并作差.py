#
# @lc app=leetcode.cn id=2894 lang=python3
# @lcpr version=30201
#
# [2894] 分类求和并作差
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(i if i % m else -i for i in range(1, n + 1))

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# 10\n3\n
# @lcpr case=end

# @lcpr case=start
# 5\n6\n
# @lcpr case=end

# @lcpr case=start
# 5\n1\n
# @lcpr case=end

#

