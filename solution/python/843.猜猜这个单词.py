#
# @lc app=leetcode.cn id=843 lang=python3
#
# [843] 猜猜这个单词
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def findSecretWord(self, words: List[str], master: "Master") -> None:
        def matches(first: str, second: str) -> int:
            return sum(a == b for a, b in zip(first, second))

        candidates = words[:]
        for _ in range(30):
            guess = min(
                candidates,
                key=lambda word: max(
                    Counter(
                        matches(word, candidate) for candidate in candidates
                    ).values()
                ),
            )
            score = master.guess(guess)
            if score == 6:
                return
            candidates = [
                candidate
                for candidate in candidates
                if matches(guess, candidate) == score
            ]


# @lc code=end


class Master:
    def __init__(self, secret: str):
        self.secret = secret
        self.guesses = 0
        self.found = False

    def guess(self, word: str) -> int:
        self.guesses += 1
        score = sum(a == b for a, b in zip(word, self.secret))
        self.found |= score == 6
        return score


if __name__ == "__main__":
    solution = Solution()
    word_lists = [
        ["acckzz", "ccbazz", "eiowzz", "abcczz", "acckaz", "accyzz"],
        [
            "abcdef",
            "acdefg",
            "adefgh",
            "aefghi",
            "afghij",
            "aghijk",
            "ahijkl",
            "aijklm",
            "ajklmn",
            "aklmno",
            "almnoz",
            "anopqr",
            "azzzzz",
        ],
    ]
    test_cases = [(word_lists[0], secret) for secret in word_lists[0]] + [
        (word_lists[1], "azzzzz")
    ]
    all_passed = True
    for idx, (words, secret) in enumerate(test_cases):
        master = Master(secret)
        solution.findSecretWord(words, master)
        try:
            assert master.found and master.guesses <= 10
            print(
                f"测试用例 {idx + 1} 通过: secret = {secret}, guesses = {master.guesses}"
            )
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: secret = {secret}")
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
