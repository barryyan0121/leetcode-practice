#
# @lc app=leetcode.cn id=514 lang=python3
# @lcpr version=30203
#
# [514] 自由之路
#

import sys
import os
from collections import defaultdict
from functools import lru_cache

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        positions = defaultdict(list)
        for idx, ch in enumerate(ring):
            positions[ch].append(idx)

        n = len(ring)

        @lru_cache(maxsize=None)
        def dp(key_idx: int, ring_idx: int) -> int:
            if key_idx == len(key):
                return 0

            best = float("inf")
            target = key[key_idx]
            for next_idx in positions[target]:
                diff = abs(next_idx - ring_idx)
                rotate = min(diff, n - diff)
                best = min(best, rotate + 1 + dp(key_idx + 1, next_idx))
            return best

        return dp(0, 0)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (solution.findRotateSteps, ("godding", "gd"), 4),
        (solution.findRotateSteps, ("abcde", "ade"), 6),
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
# ring = "godding", key = "gd"\n
# @lcpr case=end
#
