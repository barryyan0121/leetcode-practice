#
# @lc app=leetcode.cn id=411 lang=python3
# @lcpr version=30203
#
# [411] 最短独占单词缩写
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        n = len(target)
        diffs = []
        for word in dictionary:
            if len(word) != n:
                continue
            diff = 0
            for i, (a, b) in enumerate(zip(target, word)):
                if a != b:
                    diff |= 1 << i
            if diff:
                diffs.append(diff)

        if not diffs:
            return str(n)

        def abbr_len(mask: int) -> int:
            length = 0
            run = 0
            for i in range(n):
                if mask & (1 << i):
                    if run:
                        length += len(str(run))
                        run = 0
                    length += 1
                else:
                    run += 1
            if run:
                length += len(str(run))
            return length

        def build(mask: int) -> str:
            parts = []
            run = 0
            for i, ch in enumerate(target):
                if mask & (1 << i):
                    if run:
                        parts.append(str(run))
                        run = 0
                    parts.append(ch)
                else:
                    run += 1
            if run:
                parts.append(str(run))
            return "".join(parts)

        best_mask = (1 << n) - 1
        best_len = abbr_len(best_mask)

        def dfs(mask: int) -> None:
            nonlocal best_mask, best_len

            cur_len = abbr_len(mask)
            if cur_len >= best_len:
                return

            conflict = None
            for diff in diffs:
                if mask & diff == 0:
                    if conflict is None or diff.bit_count() < conflict.bit_count():
                        conflict = diff

            if conflict is None:
                best_mask = mask
                best_len = cur_len
                return

            bits = conflict & ~mask
            while bits:
                bit = bits & -bits
                bits -= bit
                dfs(mask | bit)

        dfs(0)
        return build(best_mask)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.minAbbreviation, ("apple", ["blade"]), "a4"),
        (solution.minAbbreviation, ("apple", ["plain", "amber", "blade"]), "1p3"),
        (solution.minAbbreviation, ("apple", []), "5"),
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
# apple\n["blade"]\n
# @lcpr case=end

#
