#
# @lc app=leetcode.cn id=567 lang=python3
# @lcpr version=30203
#
# [567] 字符串的排列
#

import os
import sys
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        left = 0
        matched = 0
        target = len(need)

        for right, ch in enumerate(s2):
            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    matched += 1

            while right - left + 1 > len(s1):
                left_ch = s2[left]
                if left_ch in need:
                    if window[left_ch] == need[left_ch]:
                        matched -= 1
                    window[left_ch] -= 1
                left += 1

            if matched == target and right - left + 1 == len(s1):
                return True

        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.checkInclusion, ("ab", "eidbaooo"), True),
        (solution.checkInclusion, ("ab", "eidboaoo"), False),
        (solution.checkInclusion, ("adc", "dcda"), True),
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
# s1 = "ab", s2 = "eidbaooo"\n
# @lcpr case=end
#
