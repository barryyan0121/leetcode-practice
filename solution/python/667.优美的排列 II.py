#
# @lc app=leetcode.cn id=667 lang=python3
# @lcpr version=30203
#
# [667] 优美的排列 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1, n - k))
        left, right = n - k, n
        while left <= right:
            ans.append(left)
            left += 1
            if left <= right:
                ans.append(right)
                right -= 1
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def count_diffs(nums: List[int]) -> int:
        return len({abs(nums[i] - nums[i - 1]) for i in range(1, len(nums))})

    test_cases = [
        (solution.constructArray, (3, 1), 1),
        (solution.constructArray, (3, 2), 2),
        (solution.constructArray, (5, 3), 3),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert sorted(result) == list(range(1, args[0] + 1))
            assert count_diffs(result) == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)
