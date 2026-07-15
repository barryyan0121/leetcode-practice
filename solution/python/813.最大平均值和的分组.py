#
# @lc app=leetcode.cn id=813 lang=python3
#
# [813] 最大平均值和的分组
#

import os
import sys
from functools import cache
from typing import List


# @lc code=start
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefix = [0]
        for number in nums:
            prefix.append(prefix[-1] + number)

        @cache
        def best(start: int, groups: int) -> float:
            if groups == 1:
                return (prefix[-1] - prefix[start]) / (len(nums) - start)
            return max(
                (prefix[end] - prefix[start]) / (end - start) + best(end, groups - 1)
                for end in range(start + 1, len(nums) - groups + 2)
            )

        return best(0, k)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.largestSumOfAverages, ([9, 1, 2, 3, 9], 3), 20.0),
        (solution.largestSumOfAverages, ([1, 2, 3, 4, 5, 6, 7], 4), 20.5),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert abs(result - expected) < 1e-8
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
