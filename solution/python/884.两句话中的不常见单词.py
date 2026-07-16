#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts = Counter((s1 + " " + s2).split())
        return [word for word, count in counts.items() if count == 1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.uncommonFromSentences,
            ("this apple is sweet", "this apple is sour"),
            ["sweet", "sour"],
        ),
        (solution.uncommonFromSentences, ("apple apple", "banana"), ["banana"]),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert sorted(result) == sorted(expected)
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
