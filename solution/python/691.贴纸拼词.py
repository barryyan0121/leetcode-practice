#
# @lc app=leetcode.cn id=691 lang=python3
#
# [691] 贴纸拼词
#

import os
import sys
from collections import Counter
from functools import lru_cache
from typing import *


# @lc code=start
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        counts = [Counter(sticker) for sticker in stickers]

        @lru_cache(None)
        def solve(remaining: str) -> int:
            if not remaining:
                return 0
            needed = Counter(remaining)
            best = float("inf")
            for sticker in counts:
                if remaining[0] not in sticker:
                    continue
                rest = "".join(
                    char * max(0, count - sticker[char])
                    for char, count in sorted(needed.items())
                )
                best = min(best, 1 + solve(rest))
            return best

        answer = solve("".join(sorted(target)))
        return -1 if answer == float("inf") else answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minStickers, (["with", "example", "science"], "thehat"), 3),
        (solution.minStickers, (["notice", "possible"], "basicbasic"), -1),
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
