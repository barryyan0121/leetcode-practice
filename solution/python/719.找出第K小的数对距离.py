#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 K 小的数对距离
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count(distance: int) -> int:
            total = left = 0
            for right, number in enumerate(nums):
                while number - nums[left] > distance:
                    left += 1
                total += right - left
            return total

        low, high = 0, nums[-1] - nums[0]
        while low < high:
            middle = (low + high) // 2
            if count(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.smallestDistancePair, ([1, 3, 1], 1), 0),
        (solution.smallestDistancePair, ([1, 1, 1], 2), 0),
        (solution.smallestDistancePair, ([1, 6, 1], 3), 5),
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
