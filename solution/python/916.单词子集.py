#
# @lc app=leetcode.cn id=916 lang=python3
#
# [916] 单词子集
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = Counter()
        for word in words2:
            required |= Counter(word)
        return [word for word in words1 if Counter(word) >= required]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.wordSubsets,
            (["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]),
            ["facebook", "google", "leetcode"],
        ),
        (
            solution.wordSubsets,
            (["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]),
            ["apple", "google", "leetcode"],
        ),
        (
            solution.wordSubsets,
            (["acaac", "cccbb", "aacbb", "caacc", "bcbbb"], ["c", "cc", "b"]),
            ["cccbb"],
        ),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
