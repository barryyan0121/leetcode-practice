#
# @lc app=leetcode.cn id=689 lang=python3
#
# [689] 三个无重叠子数组的最大和
#

import os
import sys

from typing import *


# @lc code=start
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        window = [sum(nums[:k])]
        for i in range(k, len(nums)):
            window.append(window[-1] + nums[i] - nums[i - k])

        left = [0] * len(window)
        for i in range(1, len(window)):
            left[i] = i if window[i] > window[left[i - 1]] else left[i - 1]

        right = [0] * len(window)
        right[-1] = len(window) - 1
        for i in range(len(window) - 2, -1, -1):
            right[i] = i if window[i] >= window[right[i + 1]] else right[i + 1]

        answer = [-1, -1, -1]
        best = -1
        for middle in range(k, len(window) - k):
            indices = [left[middle - k], middle, right[middle + k]]
            total = sum(window[i] for i in indices)
            if total > best:
                best, answer = total, indices
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxSumOfThreeSubarrays, ([1, 2, 1, 2, 6, 7, 5, 1], 2), [0, 3, 5]),
        (solution.maxSumOfThreeSubarrays, ([1, 2, 1, 2, 1, 2, 1, 2, 1], 2), [0, 2, 4]),
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
