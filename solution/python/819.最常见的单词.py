#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

import os
import re
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)
        counts = Counter(
            word
            for word in re.findall(r"[a-z]+", paragraph.lower())
            if word not in banned_words
        )
        return max(counts, key=counts.get)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.mostCommonWord,
            ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]),
            "ball",
        ),
        (solution.mostCommonWord, ("a.", []), "a"),
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
