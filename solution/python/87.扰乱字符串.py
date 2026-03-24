#
# @lc app=leetcode.cn id=87 lang=python3
# @lcpr version=30202
#
# [87] 扰乱字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from functools import lru_cache
from common.node import *


# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        n = len(s1)
        if s1 == s2:
            return True

        def prefix_counts(s: str) -> List[List[int]]:
            pref = [[0] * 26]
            for ch in s:
                cur = pref[-1][:]
                cur[ord(ch) - ord("a")] += 1
                pref.append(cur)
            return pref

        p1 = prefix_counts(s1)
        p2 = prefix_counts(s2)

        def same_counts(a: int, b: int, length: int) -> bool:
            for i in range(26):
                if p1[a + length][i] - p1[a][i] != p2[b + length][i] - p2[b][i]:
                    return False
            return True

        @lru_cache(None)
        def dfs(i: int, j: int, length: int) -> bool:
            if s1[i : i + length] == s2[j : j + length]:
                return True
            if not same_counts(i, j, length):
                return False
            for split in range(1, length):
                if dfs(i, j, split) and dfs(i + split, j + split, length - split):
                    return True
                if dfs(i, j + length - split, split) and dfs(
                    i + split, j, length - split
                ):
                    return True
            return False

        return dfs(0, 0, n)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.isScramble, ["great", "rgeat"], True),
        (solution.isScramble, ["abcde", "caebd"], False),
        (solution.isScramble, ["a", "a"], True),
        (solution.isScramble, ["abc", "bca"], True),
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
# "great"\n"rgeat"\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n"caebd"\n
# @lcpr case=end

#
