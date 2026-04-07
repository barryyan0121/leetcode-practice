#
# @lc app=leetcode.cn id=336 lang=python3
# @lcpr version=30203
#
# [336] 回文对
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        index = {word: i for i, word in enumerate(words)}
        res = set()

        def is_pal(s: str) -> bool:
            return s == s[::-1]

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                if is_pal(prefix):
                    rev = suffix[::-1]
                    if rev in index and index[rev] != i:
                        res.add((index[rev], i))
                if j != len(word) and is_pal(suffix):
                    rev = prefix[::-1]
                    if rev in index and index[rev] != i:
                        res.add((i, index[rev]))
        return [list(pair) for pair in sorted(res)]
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.palindromePairs, [["abcd", "dcba", "lls", "s", "sssll"]], [[0, 1], [1, 0], [3, 2], [2, 4]]),
        (solution.palindromePairs, [["bat", "tab", "cat"]], [[0, 1], [1, 0]]),
        (solution.palindromePairs, [["a", ""]], [[0, 1], [1, 0]]),
    ]

    def normalize(pairs: List[List[int]]) -> List[List[int]]:
        return sorted([list(pair) for pair in sorted(tuple(p) for p in pairs)])

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
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
# ["abcd","dcba","lls","s","sssll"]\n
# @lcpr case=end

#
