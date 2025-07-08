#
# @lc app=leetcode.cn id=3333 lang=python3
# @lcpr version=30201
#
# [3333] 找到初始输入字符串 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        n, cnt = len(word), 1
        freq = list()

        for i in range(1, n):
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                freq.append(cnt)
                cnt = 1
        freq.append(cnt)

        ans = 1
        for o in freq:
            ans = ans * o % mod

        if len(freq) >= k:
            return ans

        f, g = [1] + [0] * (k - 1), [1] * k
        for i in range(len(freq)):
            f_new = [0] * k
            for j in range(1, k):
                f_new[j] = g[j - 1]
                if j - freq[i] - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j - freq[i] - 1]) % mod
            g_new = [f_new[0]] + [0] * (k - 1)
            for j in range(1, k):
                g_new[j] = (g_new[j - 1] + f_new[j]) % mod
            f, g = f_new, g_new
        return (ans - g[k - 1]) % mod


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "aabbccdd"\n7\n
# @lcpr case=end

# @lcpr case=start
# "aabbccdd"\n8\n
# @lcpr case=end

# @lcpr case=start
# "aaabbb"\n3\n
# @lcpr case=end

#

