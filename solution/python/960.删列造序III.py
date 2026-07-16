#
# @lc app=leetcode.cn id=960 lang=python3
#
# [960] 删列造序 III
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns = len(strs[0])
        longest = [1] * columns
        for right in range(columns):
            for left in range(right):
                if all(word[left] <= word[right] for word in strs):
                    longest[right] = max(longest[right], longest[left] + 1)
        return columns - max(longest)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minDeletionSize, (["babca", "bbazb"],), 3),
        (solution.minDeletionSize, (["edcba"],), 4),
        (solution.minDeletionSize, (["ghi", "def", "abc"],), 0),
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
