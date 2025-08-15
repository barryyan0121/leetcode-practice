#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30202
#
# [3] 无重复字符的最长子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.lengthOfLongestSubstring, ("abcabcbb",), 3),
        (solution.lengthOfLongestSubstring, ("bbbbb",), 1),
        (solution.lengthOfLongestSubstring, ("pwwkew",), 3),
        (solution.lengthOfLongestSubstring, ("",), 0),
        (solution.lengthOfLongestSubstring, ("a",), 1),
        (solution.lengthOfLongestSubstring, ("abcdefg",), 7),
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
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#
