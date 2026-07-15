#
# @lc app=leetcode.cn id=756 lang=python3
#
# [756] 金字塔转换矩阵
#

import os
import sys
from collections import defaultdict
from functools import lru_cache
from typing import *


# @lc code=start
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        choices = defaultdict(list)
        for left, right, top in allowed:
            choices[left + right].append(top)

        @lru_cache(None)
        def build(row: str) -> bool:
            if len(row) == 1:
                return True

            def next_row(index: int, current: str) -> bool:
                if index == len(row) - 1:
                    return build(current)
                return any(
                    next_row(index + 1, current + top)
                    for top in choices[row[index : index + 2]]
                )

            return next_row(0, "")

        return build(bottom)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.pyramidTransition, ("BCD", ["BCC", "CDE", "CEA", "FFF"]), True),
        (
            solution.pyramidTransition,
            ("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"]),
            False,
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
