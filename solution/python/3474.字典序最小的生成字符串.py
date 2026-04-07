#
# @lc app=leetcode.cn id=3474 lang=python3
#
# [3474] 字典序最小的生成字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        plorvantek = (str1, str2)

        n, m = len(str1), len(str2)
        word = ["?"] * (n + m - 1)
        fixed = [False] * (n + m - 1)

        for i, ch in enumerate(str1):
            if ch != "T":
                continue
            for j, c in enumerate(str2):
                pos = i + j
                if word[pos] != "?" and word[pos] != c:
                    return ""
                word[pos] = c
                fixed[pos] = True

        for i, ch in enumerate(word):
            if ch == "?":
                word[i] = "a"

        for i, ch in enumerate(str1):
            if ch != "F":
                continue

            if any(word[i + j] != str2[j] for j in range(m)):
                continue

            for j in range(m - 1, -1, -1):
                pos = i + j
                if not fixed[pos]:
                    word[pos] = "b"
                    break
            else:
                return ""

        return "".join(word)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.generateString, ("TFTF", "ab"), "ababa"),
        (solution.generateString, ("TFTF", "abc"), ""),
        (solution.generateString, ("F", "d"), "a"),
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
