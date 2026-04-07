#
# @lc app=leetcode.cn id=345 lang=python3
# @lcpr version=30203
#
# [345] 反转字符串中的元音字母
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        left, right = 0, len(chars) - 1

        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return "".join(chars)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.reverseVowels, ("hello",), "holle"),
        (solution.reverseVowels, ("leetcode",), "leotcede"),
        (solution.reverseVowels, ("aA",), "Aa"),
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
# "hello"\n
# @lcpr case=end
