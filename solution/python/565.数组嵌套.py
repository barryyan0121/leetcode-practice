#
# @lc app=leetcode.cn id=565 lang=python3
# @lcpr version=30203
#
# [565] 数组嵌套
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        best = 0
        visited = [False] * len(nums)

        for i in range(len(nums)):
            if visited[i]:
                continue
            length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = nums[j]
                length += 1
            best = max(best, length)

        return best


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.arrayNesting, ([5, 4, 0, 3, 1, 6, 2],), 4),
        (solution.arrayNesting, ([0, 1, 2],), 1),
        (solution.arrayNesting, ([1, 0, 3, 2],), 2),
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


#
# @lcpr case=start
# [5,4,0,3,1,6,2]\n
# @lcpr case=end
#
