#
# @lc app=leetcode.cn id=2273 lang=python3
# @lcpr version=30203
#
# [2273] 移除字母异位词后的结果数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        curr_word = ""
        result = []
        for word in words:
            sorted_word = "".join(sorted(word))
            if sorted_word != curr_word:
                result.append(word)
                curr_word = sorted_word
        return result
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.removeAnagrams,
            (["abba", "baba", "bbaa", "cd", "cd"],),
            ["abba", "cd"],
        ),
        (
            solution.removeAnagrams,
            (["a", "b", "c", "d", "e"],),
            ["a", "b", "c", "d", "e"],
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
# ["abba","baba","bbaa","cd","cd"]\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","c","d","e"]\n
# @lcpr case=end

#
