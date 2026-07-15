#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        buckets = [0] * k

        def place(index: int) -> bool:
            if index == len(nums):
                return True
            for bucket in range(k):
                if buckets[bucket] + nums[index] > target:
                    continue
                buckets[bucket] += nums[index]
                if place(index + 1):
                    return True
                buckets[bucket] -= nums[index]
                if buckets[bucket] == 0:
                    break
            return False

        return place(0)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.canPartitionKSubsets, ([4, 3, 2, 3, 5, 2, 1], 4), True),
        (solution.canPartitionKSubsets, ([1, 2, 3, 4], 3), False),
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
