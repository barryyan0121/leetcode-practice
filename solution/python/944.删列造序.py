#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(
            any(first > second for first, second in zip(column, column[1:]))
            for column in zip(*strs)
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minDeletionSize, (["cba", "daf", "ghi"],), 1),
        (solution.minDeletionSize, (["a", "b"],), 0),
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
