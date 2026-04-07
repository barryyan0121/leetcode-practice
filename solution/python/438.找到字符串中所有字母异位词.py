#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30203
#
# [438] 找到字符串中所有字母异位词
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = Counter()
        left = 0
        res = []
        for right, ch in enumerate(s):
            window[ch] += 1
            while right - left + 1 > len(p):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            if right - left + 1 == len(p) and window == need:
                res.append(left)
        return res


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findAnagrams, ["cbaebabacd", "abc"], [0, 6]),
        (solution.findAnagrams, ["abab", "ab"], [0, 1, 2]),
        (solution.findAnagrams, ["af", "be"], []),
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
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

#
