#
# @lc app=leetcode.cn id=890 lang=python3
#
# [890] 查找和替换模式
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def shape(word: str) -> List[int]:
            first = {}
            return [first.setdefault(character, len(first)) for character in word]

        target = shape(pattern)
        return [word for word in words if shape(word) == target]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findAndReplacePattern,
            (["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"),
            ["mee", "aqq"],
        ),
        (solution.findAndReplacePattern, (["a", "b", "c"], "a"), ["a", "b", "c"]),
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
