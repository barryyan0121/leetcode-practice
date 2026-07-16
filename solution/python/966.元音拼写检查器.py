#
# @lc app=leetcode.cn id=966 lang=python3
#
# [966] 元音拼写检查器
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        lowercase = {}
        vowel_errors = {}

        def mask(word):
            return "".join(
                "*" if character in "aeiou" else character for character in word.lower()
            )

        for word in wordlist:
            lowercase.setdefault(word.lower(), word)
            vowel_errors.setdefault(mask(word), word)

        answer = []
        for query in queries:
            if query in exact:
                answer.append(query)
            elif query.lower() in lowercase:
                answer.append(lowercase[query.lower()])
            else:
                answer.append(vowel_errors.get(mask(query), ""))
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.spellchecker,
            (
                ["KiTe", "kite", "hare", "Hare"],
                [
                    "kite",
                    "Kite",
                    "KiTe",
                    "Hare",
                    "HARE",
                    "Hear",
                    "hear",
                    "keti",
                    "keet",
                    "keto",
                ],
            ),
            ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"],
        ),
        (
            solution.spellchecker,
            (["yellow"], ["YellOw", "yollow", "yllw"]),
            ["yellow", "yellow", ""],
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
