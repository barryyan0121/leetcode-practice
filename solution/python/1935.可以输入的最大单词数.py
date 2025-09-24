#
# @lc app=leetcode.cn id=1935 lang=python3
# @lcpr version=30203
#
# [1935] 可以输入的最大单词数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        broken_set = set(brokenLetters)
        count = 0
        for word in words:
            if not any(char in broken_set for char in word):
                count += 1
        return count
        # @lc code=end
        pass


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.canBeTypedWords, ("hello world", "ad"), 1),
        (solution.canBeTypedWords, ("leet code", "lt"), 1),
        (solution.canBeTypedWords, ("leet code", "e"), 0),
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
# "hello world"\n"ad"\n
# @lcpr case=end

# @lcpr case=start
# "leet code"\n"lt"\n
# @lcpr case=end

# @lcpr case=start
# "leet code"\n"e"\n
# @lcpr case=end

#
