#
# @lc app=leetcode.cn id=555 lang=python3
# @lcpr version=30203
#
# [555] 分割连接字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        parts = [max(s, s[::-1]) for s in strs]
        best = ""
        for i, original in enumerate(strs):
            rest = "".join(parts[:i] + parts[i + 1 :])
            for current in (original, original[::-1]):
                for j in range(len(current)):
                    cur = current[j:] + rest + current[:j]
                    if cur > best:
                        best = cur
        return best


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def brute_force(strs: List[str]) -> str:
        from itertools import product

        best = ""
        for mask in product([0, 1], repeat=len(strs)):
            merged = "".join(s[::-1] if bit else s for s, bit in zip(strs, mask))
            for i in range(len(merged)):
                cur = merged[i:] + merged[:i]
                if cur > best:
                    best = cur
        return best

    test_cases = [
        (solution.splitLoopedString, (["abc"],), brute_force(["abc"])),
        (solution.splitLoopedString, (["abc", "xyz"],), brute_force(["abc", "xyz"])),
        (
            solution.splitLoopedString,
            (["lc", "eetcode"],),
            brute_force(["lc", "eetcode"]),
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
# ["abc","xyz"]\n
# @lcpr case=end
#
