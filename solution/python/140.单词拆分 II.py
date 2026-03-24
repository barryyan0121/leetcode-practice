#
# @lc app=leetcode.cn id=140 lang=python3
# @lcpr version=30203
#
# [140] 单词拆分 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def dfs(start: int) -> List[str]:
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]

            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word not in words:
                    continue
                for suffix in dfs(end):
                    if suffix:
                        result.append(word + " " + suffix)
                    else:
                        result.append(word)

            memo[start] = result
            return result

        return dfs(0)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(words: List[str]) -> List[str]:
        return sorted(words)

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.wordBreak,
            ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
            ["cats and dog", "cat sand dog"],
        ),
        (
            solution.wordBreak,
            ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
            ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
        ),
        (solution.wordBreak, ("catsandog", ["cats", "dog", "sand", "and", "cat"]), []),
    ]

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
# "catsanddog"\n["cat","cats","and","sand","dog"]\n
# @lcpr case=end
