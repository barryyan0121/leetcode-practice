#
# @lc app=leetcode.cn id=1394 lang=python3
# @lcpr version=30201
#
# [1394] 找出数组中的幸运数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *
from collections import Counter


# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        for num in sorted(counter.keys(), reverse=True):
            if counter[num] == num:
                return num
        return -1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# [2,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,3,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [5]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#
