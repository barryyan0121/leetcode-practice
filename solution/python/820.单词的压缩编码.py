#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        remaining = set(words)
        for word in words:
            for index in range(1, len(word)):
                remaining.discard(word[index:])
        return sum(len(word) + 1 for word in remaining)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minimumLengthEncoding, (["time", "me", "bell"],), 10),
        (solution.minimumLengthEncoding, (["t"],), 2),
        (solution.minimumLengthEncoding, (["time", "time"],), 5),
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
