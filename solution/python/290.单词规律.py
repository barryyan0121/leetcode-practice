#
# @lc app=leetcode.cn id=290 lang=python3
# @lcpr version=30203
#
# [290] 单词规律
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        p2w = {}
        w2p = {}
        for p, w in zip(pattern, words):
            if (p in p2w and p2w[p] != w) or (w in w2p and w2p[w] != p):
                return False
            p2w[p] = w
            w2p[w] = p
        return True
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.wordPattern, ["abba", "dog cat cat dog"], True),
        (solution.wordPattern, ["abba", "dog cat cat fish"], False),
        (solution.wordPattern, ["aaaa", "dog cat cat dog"], False),
        (solution.wordPattern, ["abba", "dog dog dog dog"], False),
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
# "abba"\n"dog cat cat dog"\n
# @lcpr case=end

#
