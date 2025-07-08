#
# @lc app=leetcode.cn id=2081 lang=python3
# @lcpr version=30201
#
# [2081] k 镜像数字的和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPalindrome(x: int) -> bool:
            digit = list()
            while x:
                digit.append(x % k)
                x //= k
            return digit == digit[::-1]

        left, cnt, ans = 1, 0, 0
        while cnt < n:
            right = left * 10
            # op = 0 表示枚举奇数长度回文，op = 1 表示枚举偶数长度回文
            for op in [0, 1]:
                # 枚举 i'
                for i in range(left, right):
                    if cnt == n:
                        break

                    combined = i
                    x = (i // 10 if op == 0 else i)
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if isPalindrome(combined):
                        cnt += 1
                        ans += combined
            left = right

        return ans

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# 2\n5\n
# @lcpr case=end

# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 7\n17\n
# @lcpr case=end

#

