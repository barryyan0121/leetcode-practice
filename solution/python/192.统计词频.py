#
# @lc app=leetcode.cn id=192 lang=python3
# @lcpr version=30202
#
# [192] 统计词频
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *


# @lc code=start
class Solution:
    def wordFrequency(self, text: str) -> List[List[Union[str, int]]]:
        counts = Counter(text.split())
        return [
            [word, freq]
            for word, freq in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        ]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.wordFrequency,
            ("the day is sunny the the the sunny is is",),
            [["the", 4], ["is", 3], ["sunny", 2], ["day", 1]],
        ),
        (solution.wordFrequency, ("hello",), [["hello", 1]]),
    ]

    for i, (func, args, want) in enumerate(test_cases):
        got = func(*args)
        assert got == want, (i, args, got, want)
