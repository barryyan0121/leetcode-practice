#
# @lc app=leetcode.cn id=318 lang=python3
# @lcpr version=30203
#
# [318] 最大单词长度乘积
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        lengths = []
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord("a"))
            masks.append(mask)
            lengths.append(len(word))

        best = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    best = max(best, lengths[i] * lengths[j])
        return best


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxProduct, (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],), 16),
        (solution.maxProduct, (["a", "ab", "abc", "d", "cd", "bcd", "abcd"],), 4),
        (solution.maxProduct, (["a", "aa", "aaa", "aaaa"],), 0),
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
# ["abcw","baz","foo","bar","xtfn","abcdef"]\n
# @lcpr case=end
