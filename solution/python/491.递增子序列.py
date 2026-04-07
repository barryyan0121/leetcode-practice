#
# @lc app=leetcode.cn id=491 lang=python3
# @lcpr version=30203
#
# [491] 递增子序列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def dfs(start: int) -> None:
            if len(path) >= 2:
                ans.append(path[:])
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if path and nums[i] < path[-1]:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findSubsequences,
            ([4, 6, 7, 7],),
            [
                [4, 6],
                [4, 6, 7],
                [4, 6, 7, 7],
                [4, 7],
                [4, 7, 7],
                [6, 7],
                [6, 7, 7],
                [7, 7],
            ],
        ),
        (solution.findSubsequences, ([4, 4, 3, 2, 1],), [[4, 4]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert sorted(map(tuple, result)) == sorted(map(tuple, expected))
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


#
# @lcpr case=start
# [4,6,7,7]\n
# @lcpr case=end

#
