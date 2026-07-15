#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第 K 个语法符号
#

import os
import sys


# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return (k - 1).bit_count() & 1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.kthGrammar, (1, 1), 0),
        (solution.kthGrammar, (2, 1), 0),
        (solution.kthGrammar, (2, 2), 1),
        (solution.kthGrammar, (4, 5), 1),
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
