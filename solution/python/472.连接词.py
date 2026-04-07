#
# @lc app=leetcode.cn id=472 lang=python3
# @lcpr version=30203
#
# [472] 连接词
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        word_set = set()
        res = []

        def can_form(word: str) -> bool:
            if not word_set:
                return False
            dp = [False] * (len(word) + 1)
            dp[0] = True
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[-1]

        for word in words:
            if can_form(word):
                res.append(word)
            word_set.add(word)
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findAllConcatenatedWordsInADict,
            [
                [
                    "cat",
                    "cats",
                    "catsdogcats",
                    "dog",
                    "dogcatsdog",
                    "hippopotamuses",
                    "rat",
                    "ratcatdogcat",
                ]
            ],
            ["catsdogcats", "dogcatsdog", "ratcatdogcat"],
        ),
        (solution.findAllConcatenatedWordsInADict, [["a", "b", "ab"]], ["ab"]),
    ]

    def normalize(words: List[str]) -> List[str]:
        return sorted(words)

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
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]\n
# @lcpr case=end

#
