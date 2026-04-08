#
# @lc app=leetcode.cn id=522 lang=python3
# @lcpr version=30203
#
# [522] 最长特殊序列 II
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def _is_subsequence(self, small: str, large: str) -> bool:
        it = iter(large)
        return all(ch in it for ch in small)

    def findLUSlength(self, strs: List[str]) -> int:
        counts = Counter(strs)
        for word in sorted(strs, key=lambda s: (-len(s), s)):
            if counts[word] > 1:
                continue
            if all(
                word == other or not self._is_subsequence(word, other) for other in strs
            ):
                return len(word)
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findLUSlength, (["aba", "cdc", "eae"],), 3),
        (solution.findLUSlength, (["aaa", "aaa", "aa"],), -1),
        (solution.findLUSlength, (["aabbcc", "aabbcc", "cb", "abc"],), 2),
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
# ["aba","cdc","eae"]\n
# @lcpr case=end
#
