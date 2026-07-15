#
# @lc app=leetcode.cn id=809 lang=python3
#
# [809] 情感丰富的文字
#

import os
import sys
from itertools import groupby
from typing import List


# @lc code=start
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def groups(word: str) -> List[tuple[str, int]]:
            return [(character, len(list(group))) for character, group in groupby(word)]

        target = groups(s)
        answer = 0
        for word in words:
            candidate = groups(word)
            answer += len(candidate) == len(target) and all(
                target_character == candidate_character
                and target_count >= candidate_count
                and (target_count == candidate_count or target_count >= 3)
                for (target_character, target_count), (
                    candidate_character,
                    candidate_count,
                ) in zip(target, candidate)
            )
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.expressiveWords, ("heeellooo", ["hello", "hi", "helo"]), 1),
        (solution.expressiveWords, ("zzzzzyyyyy", ["zzyy", "zy", "zyy"]), 3),
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
