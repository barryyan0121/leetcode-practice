#
# @lc app=leetcode.cn id=848 lang=python3
#
# [848] 字母移位
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = 0
        answer = list(s)
        for index in range(len(s) - 1, -1, -1):
            total = (total + shifts[index]) % 26
            answer[index] = chr((ord(s[index]) - ord("a") + total) % 26 + ord("a"))
        return "".join(answer)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.shiftingLetters, ("abc", [3, 5, 9]), "rpl"),
        (solution.shiftingLetters, ("aaa", [1, 2, 3]), "gfd"),
        (solution.shiftingLetters, ("z", [1]), "a"),
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
