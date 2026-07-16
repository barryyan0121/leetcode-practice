#
# @lc app=leetcode.cn id=891 lang=python3
#
# [891] 子序列宽度之和
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        power = 1
        for left, right in zip(nums, reversed(nums)):
            answer += (left - right) * power
            power = power * 2 % 1_000_000_007
        return answer % 1_000_000_007


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.sumSubseqWidths, ([2, 1, 3],), 6),
        (solution.sumSubseqWidths, ([2],), 0),
        (solution.sumSubseqWidths, ([1, 2, 3, 4],), 23),
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
