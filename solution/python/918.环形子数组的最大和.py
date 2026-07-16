#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        maximum = minimum = maximum_ending = minimum_ending = nums[0]
        for number in nums[1:]:
            maximum_ending = max(number, maximum_ending + number)
            minimum_ending = min(number, minimum_ending + number)
            maximum = max(maximum, maximum_ending)
            minimum = min(minimum, minimum_ending)
            total += number
        return maximum if maximum < 0 else max(maximum, total - minimum)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxSubarraySumCircular, ([1, -2, 3, -2],), 3),
        (solution.maxSubarraySumCircular, ([5, -3, 5],), 10),
        (solution.maxSubarraySumCircular, ([-3, -2, -3],), -2),
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
