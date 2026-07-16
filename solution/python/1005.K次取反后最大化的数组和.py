#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for index in range(len(nums)):
            if nums[index] >= 0 or k == 0:
                break
            nums[index] = -nums[index]
            k -= 1
        return sum(nums) - 2 * (k % 2) * min(map(abs, nums))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.largestSumAfterKNegations, ([4, 2, 3], 1), 5),
        (solution.largestSumAfterKNegations, ([3, -1, 0, 2], 3), 6),
        (solution.largestSumAfterKNegations, ([2, -3, -1, 5, -4], 2), 13),
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
