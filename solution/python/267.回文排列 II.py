#
# @lc app=leetcode.cn id=267 lang=python3
# @lcpr version=30203
#
# [267] 回文排列 II
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        odd_chars = [char for char, count in counter.items() if count % 2 == 1]
        if len(odd_chars) > 1:
            return []

        middle = odd_chars[0] if odd_chars else ""
        half = []
        for char, count in counter.items():
            half.extend(char for _ in range(count // 2))
        half.sort()

        result = []
        used = [False] * len(half)

        def backtrack(path: List[str]) -> None:
            if len(path) == len(half):
                left = "".join(path)
                result.append(left + middle + left[::-1])
                return

            for i in range(len(half)):
                if used[i]:
                    continue
                if i > 0 and half[i] == half[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(half[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(words: List[str]) -> List[str]:
        return sorted(words)

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.generatePalindromes, ("aabb",), ["abba", "baab"]),
        (solution.generatePalindromes, ("abc",), []),
        (solution.generatePalindromes, ("aaa",), ["aaa"]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
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
# "aabb"\n
# @lcpr case=end
