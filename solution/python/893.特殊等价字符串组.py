#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        return len(
            {(tuple(sorted(word[::2])), tuple(sorted(word[1::2]))) for word in words}
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.numSpecialEquivGroups,
            (["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"],),
            3,
        ),
        (
            solution.numSpecialEquivGroups,
            (["abc", "acb", "bac", "bca", "cab", "cba"],),
            3,
        ),
        (solution.numSpecialEquivGroups, (["a", "a"],), 1),
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
