#
# @lc app=leetcode.cn id=395 lang=python3
# @lcpr version=30203
#
# [395] 至少有 K 个重复字符的最长子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import Counter
from common.node import *


# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] < k:
                return max(
                    self.longestSubstring(s[:i], k),
                    self.longestSubstring(s[i + 1 :], k),
                )
        return len(s)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.longestSubstring, ("aaabb", 3), 3),
        (solution.longestSubstring, ("ababbc", 2), 5),
        (solution.longestSubstring, ("weitong", 2), 0),
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
# "aaabb"\n3\n
# @lcpr case=end
