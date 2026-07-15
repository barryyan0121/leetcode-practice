#
# @lc app=leetcode.cn id=791 lang=python3
#
# [791] 自定义字符串排序
#

import os
import sys
from collections import Counter


# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        ordered = "".join(character * counts.pop(character, 0) for character in order)
        return ordered + "".join(
            character * count for character, count in counts.items()
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.customSortString, ("cba", "abcd"), "cbad"),
        (solution.customSortString, ("bcafg", "abcd"), "bcad"),
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
