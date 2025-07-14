#
# @lc app=leetcode.cn id=1290 lang=python3
# @lcpr version=30201
#
# [1290] 二进制链表转整数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head:
            ans = ans << 1 | head.val
            head = head.next
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # your test code here


#
# @lcpr case=start
# [1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,0]\n
# @lcpr case=end

#
