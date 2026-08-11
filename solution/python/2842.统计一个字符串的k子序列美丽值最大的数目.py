#
# @lc app=leetcode.cn id=2842 lang=python3
# @lcpr version=30203
#
# [2842] 统计一个字符串的 k 子序列美丽值最大的数目
#

import math
import os
import sys
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        frequencies = sorted(Counter(s).values(), reverse=True)
        if len(frequencies) < k:
            return 0
        cutoff = frequencies[k - 1]
        greater = frequencies[: frequencies.index(cutoff)]
        equal_count = frequencies.count(cutoff)
        need = k - len(greater)
        answer = math.comb(equal_count, need)
        for frequency in greater:
            answer = answer * frequency % mod
        return answer * pow(cutoff, need, mod) % mod


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.countKSubsequencesWithMaxBeauty("bcca", 2) == 4
    assert solution.countKSubsequencesWithMaxBeauty("abbcd", 4) == 2
    print("测试用例通过")
