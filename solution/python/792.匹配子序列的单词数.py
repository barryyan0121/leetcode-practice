#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#

import os
import sys
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for word in words:
            iterator = iter(word)
            waiting[next(iterator)].append(iterator)

        matched = 0
        for character in s:
            for iterator in waiting.pop(character, []):
                next_character = next(iterator, None)
                if next_character is None:
                    matched += 1
                else:
                    waiting[next_character].append(iterator)
        return matched


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numMatchingSubseq, ("abcde", ["a", "bb", "acd", "ace"]), 3),
        (
            solution.numMatchingSubseq,
            ("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]),
            2,
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
