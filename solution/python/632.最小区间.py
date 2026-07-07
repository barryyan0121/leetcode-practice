#
# @lc app=leetcode.cn id=632 lang=python3
# @lcpr version=30203
#
# [632] 最小区间
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        right = -(10**9)
        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            right = max(right, arr[0])
        ans = [-(10**9), 10**9]
        while True:
            left, i, j = heapq.heappop(heap)
            if right - left < ans[1] - ans[0]:
                ans = [left, right]
            if j + 1 == len(nums[i]):
                return ans
            nxt = nums[i][j + 1]
            right = max(right, nxt)
            heapq.heappush(heap, (nxt, i, j + 1))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.smallestRange,
            ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],),
            [20, 24],
        ),
        (solution.smallestRange, ([[1, 2, 3], [1, 2, 3], [1, 2, 3]],), [1, 1]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
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
