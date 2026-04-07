#
# @lc app=leetcode.cn id=288 lang=python3
# @lcpr version=30203
#
# [288] 唯一单词缩写
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import defaultdict
from common.node import *


# @lc code=start
class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.abbr_to_words = defaultdict(set)
        for word in dictionary:
            self.abbr_to_words[self._abbr(word)].add(word)

    def _abbr(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return f"{word[0]}{len(word) - 2}{word[-1]}"

    def isUnique(self, word: str) -> bool:
        words = self.abbr_to_words[self._abbr(word)]
        return not words or words == {word}
        # @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    test_cases = [
        (
            [
                ("init", [["deer", "door", "cake", "card"]]),
                ("isUnique", ["dear"]),
                ("isUnique", ["cart"]),
                ("isUnique", ["cane"]),
                ("isUnique", ["make"]),
                ("isUnique", ["cake"]),
            ],
            [None, False, True, False, True, True],
        ),
        (
            [
                ("init", [["a", "a"]]),
                ("isUnique", ["a"]),
                ("isUnique", ["b"]),
            ],
            [None, True, True],
        ),
    ]

    all_passed = True
    for idx, (ops, expected) in enumerate(test_cases):
        try:
            result = []
            obj = None
            for op, args in ops:
                if op == "init":
                    obj = ValidWordAbbr(*args)
                    result.append(None)
                else:
                    result.append(obj.isUnique(*args))
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {ops}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {ops}, 期望 = {expected}, 实际 = {result}"
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
# ["deer","door","cake","card"]\n
# @lcpr case=end

#
