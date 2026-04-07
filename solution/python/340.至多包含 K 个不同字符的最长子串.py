#
# @lc app=leetcode.cn id=340 lang=python3
# @lcpr version=30203
#
# [340] 至多包含 K 个不同字符的最长子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import defaultdict
from common.node import *


# @lc code=start
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0
        left = 0
        counts = defaultdict(int)
        ans = 0
        for right, ch in enumerate(s):
            counts[ch] += 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.lengthOfLongestSubstringKDistinct, ["eceba", 2], 3),
        (solution.lengthOfLongestSubstringKDistinct, ["aa", 1], 2),
        (solution.lengthOfLongestSubstringKDistinct, ["a", 0], 0),
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
# "eceba"\n2\n
# @lcpr case=end

#
