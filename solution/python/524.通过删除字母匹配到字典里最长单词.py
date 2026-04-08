#
# @lc app=leetcode.cn id=524 lang=python3
# @lcpr version=30203
#
# [524] 通过删除字母匹配到字典里最长单词
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def _is_subsequence(self, source: str, target: str) -> bool:
        it = iter(source)
        return all(ch in it for ch in target)

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        best = ""
        for word in sorted(dictionary, key=lambda w: (-len(w), w)):
            if self._is_subsequence(s, word):
                return word
        return best


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findLongestWord,
            ("abpcplea", ["ale", "apple", "monkey", "plea"]),
            "apple",
        ),
        (
            solution.findLongestWord,
            ("abpcplea", ["a", "b", "c"]),
            "a",
        ),
        (
            solution.findLongestWord,
            ("bab", ["ba", "ab", "a", "b"]),
            "ab",
        ),
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
# "abpcplea"\n["ale","apple","monkey","plea"]\n
# @lcpr case=end
#
