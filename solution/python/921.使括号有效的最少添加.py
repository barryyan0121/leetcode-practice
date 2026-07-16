#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

import os
import sys


# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unmatched_open = additions = 0
        for character in s:
            if character == "(":
                unmatched_open += 1
            elif unmatched_open:
                unmatched_open -= 1
            else:
                additions += 1
        return additions + unmatched_open


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minAddToMakeValid, ("())",), 1),
        (solution.minAddToMakeValid, ("(((",), 3),
        (solution.minAddToMakeValid, ("()))((",), 4),
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
