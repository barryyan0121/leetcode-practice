#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

import os
import sys
from collections import Counter


# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        differences = [index for index in range(len(s)) if s[index] != goal[index]]
        if not differences:
            return any(count > 1 for count in Counter(s).values())
        return (
            len(differences) == 2
            and s[differences[0]] == goal[differences[1]]
            and s[differences[1]] == goal[differences[0]]
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.buddyStrings, ("ab", "ba"), True),
        (solution.buddyStrings, ("ab", "ab"), False),
        (solution.buddyStrings, ("aa", "aa"), True),
        (solution.buddyStrings, ("abcd", "badc"), False),
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
