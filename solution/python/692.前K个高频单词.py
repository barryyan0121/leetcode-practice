#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

import os
import sys
from collections import Counter
from typing import *


# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        return sorted(counts, key=lambda word: (-counts[word], word))[:k]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.topKFrequent,
            (["i", "love", "leetcode", "i", "love", "coding"], 2),
            ["i", "love"],
        ),
        (
            solution.topKFrequent,
            (
                ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                4,
            ),
            ["the", "is", "sunny", "day"],
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
