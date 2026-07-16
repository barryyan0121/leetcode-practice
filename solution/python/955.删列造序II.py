#
# @lc app=leetcode.cn id=955 lang=python3
#
# [955] 删列造序 II
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        unresolved = [True] * (len(strs) - 1)
        deletions = 0
        for column in range(len(strs[0])):
            if any(
                unresolved[row] and strs[row][column] > strs[row + 1][column]
                for row in range(len(strs) - 1)
            ):
                deletions += 1
                continue
            for row in range(len(strs) - 1):
                unresolved[row] &= strs[row][column] == strs[row + 1][column]
        return deletions


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minDeletionSize, (["ca", "bb", "ac"],), 1),
        (solution.minDeletionSize, (["xc", "yb", "za"],), 0),
        (solution.minDeletionSize, (["zyx", "wvu", "tsr"],), 3),
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
