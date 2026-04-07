#
# @lc app=leetcode.cn id=424 lang=python3
# @lcpr version=30203
#
# [424] 替换后的最长重复字符
#

import sys
import os
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        left = 0
        max_freq = 0
        ans = 0
        for right, ch in enumerate(s):
            cnt[ch] += 1
            max_freq = max(max_freq, cnt[ch])
            while right - left + 1 - max_freq > k:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.characterReplacement, ["ABAB", 2], 4),
        (solution.characterReplacement, ["AABABBA", 1], 4),
        (solution.characterReplacement, ["AAAA", 2], 4),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

#
