#
# @lc app=leetcode.cn id=471 lang=python3
# @lcpr version=30203
#
# [471] 编码最短长度的字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from functools import lru_cache
from common.node import *


# @lc code=start
class Solution:
    def encode(self, s: str) -> str:
        @lru_cache(None)
        def dfs(sub: str) -> str:
            if len(sub) <= 4:
                return sub

            best = sub
            for i in range(1, len(sub)):
                cand = dfs(sub[:i]) + dfs(sub[i:])
                if len(cand) < len(best):
                    best = cand

            lps = [0] * len(sub)
            for i in range(1, len(sub)):
                j = lps[i - 1]
                while j > 0 and sub[i] != sub[j]:
                    j = lps[j - 1]
                if sub[i] == sub[j]:
                    j += 1
                lps[i] = j
            period = len(sub) - lps[-1]
            if period < len(sub) and len(sub) % period == 0:
                encoded = f"{len(sub) // period}[{dfs(sub[:period])}]"
                if len(encoded) <= len(best):
                    best = encoded
            return best

        return dfs(s)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.encode, ["aaa"], "aaa"),
        (solution.encode, ["aaaaa"], "5[a]"),
        (solution.encode, ["abcabcabc"], "3[abc]"),
        (solution.encode, ["aaaaaaaaaa"], "10[a]"),
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
# "aaaaa"\n
# @lcpr case=end

#
