#
# @lc app=leetcode.cn id=527 lang=python3
# @lcpr version=30203
#
# [527] 单词缩写
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def _abbr(self, word: str, prefix_len: int) -> str:
        if len(word) - prefix_len <= 2:
            return word
        abbr = f"{word[:prefix_len]}{len(word) - prefix_len - 1}{word[-1]}"
        return abbr if len(abbr) < len(word) else word

    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        n = len(words)
        prefix = [1] * n
        result = [self._abbr(word, 1) for word in words]

        while True:
            groups: Dict[str, List[int]] = {}
            for idx, abbr in enumerate(result):
                groups.setdefault(abbr, []).append(idx)

            changed = False
            for idxs in groups.values():
                if len(idxs) == 1:
                    continue
                for idx in idxs:
                    if prefix[idx] < len(words[idx]):
                        prefix[idx] += 1
                        changed = True

            if not changed:
                break

            result = [self._abbr(word, prefix[idx]) for idx, word in enumerate(words)]

        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def is_valid_abbr(word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)

    def run_case(words: List[str]) -> bool:
        result = solution.wordsAbbreviation(words)
        assert len(result) == len(words)
        assert len(set(result)) == len(result)
        for word, abbr in zip(words, result):
            assert is_valid_abbr(word, abbr)
            if len(word) > 3:
                assert len(abbr) <= len(word)
        return True

    test_cases = [
        (run_case, (["like", "god", "me", "internet"],), True),
        (
            run_case,
            (
                [
                    "internal",
                    "interval",
                    "intension",
                    "intrusion",
                    "face",
                    "book",
                ],
            ),
            True,
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
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
# ["like","god","internal","me","internet","interval","intension","face","intrusion"]\n
# @lcpr case=end
#
