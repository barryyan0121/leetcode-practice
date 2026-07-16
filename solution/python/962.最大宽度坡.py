#
# @lc app=leetcode.cn id=962 lang=python3
#
# [962] 最大宽度坡
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        candidates = []
        for index, number in enumerate(nums):
            if not candidates or number < nums[candidates[-1]]:
                candidates.append(index)
        answer = 0
        for right in range(len(nums) - 1, -1, -1):
            while candidates and nums[candidates[-1]] <= nums[right]:
                answer = max(answer, right - candidates.pop())
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxWidthRamp, ([6, 0, 8, 2, 1, 5],), 4),
        (solution.maxWidthRamp, ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1],), 7),
        (solution.maxWidthRamp, ([3, 2, 1],), 0),
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
