#
# @lc app=leetcode.cn id=3756 lang=python3
# @lcpr version=30203
#
# [3756] 连接非零数字并乘以其数字和 II
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        digit_sum = [0]
        nonzero_count = [0]
        values = [0]
        pow10 = [1]

        for ch in s:
            digit = ord(ch) - ord("0")
            digit_sum.append(digit_sum[-1] + digit)
            nonzero_count.append(nonzero_count[-1] + (digit != 0))
            if digit:
                values.append((values[-1] * 10 + digit) % mod)
                pow10.append(pow10[-1] * 10 % mod)

        ans = []
        for left, right in queries:
            start = nonzero_count[left]
            end = nonzero_count[right + 1]
            x = (values[end] - values[start] * pow10[end - start]) % mod
            total = digit_sum[right + 1] - digit_sum[left]
            ans.append(x * total % mod)
        return ans


# @lc code=end


if __name__ == "__main__":
    f = Solution().sumAndMultiply
    assert f("10203004", [[0, 7], [1, 3], [4, 6]]) == [12340, 4, 9]
    assert f("1000", [[0, 3], [1, 1]]) == [1, 0]
    assert f("9876543210", [[0, 9]]) == [444444137]
    assert f("0010203", [[0, 6], [2, 5], [0, 1]]) == [738, 36, 0]
