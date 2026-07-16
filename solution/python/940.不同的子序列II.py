#
# @lc app=leetcode.cn id=940 lang=python3
#
# [940] 不同的子序列 II
#

import os
import sys


# @lc code=start
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        modulo = 10**9 + 7
        total = 1
        previous = {}
        for character in s:
            added = total
            total = (2 * total - previous.get(character, 0)) % modulo
            previous[character] = added
        return (total - 1) % modulo


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.distinctSubseqII, ("abc",), 7),
        (solution.distinctSubseqII, ("aba",), 6),
        (solution.distinctSubseqII, ("aaa",), 3),
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
