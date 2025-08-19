#
# @lc app=leetcode.cn id=3355 lang=python3
# @lcpr version=30202
#
# [3355] 零数组变换 I
#

import sys
import os
from itertools import accumulate

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)
        for start, end in queries:
            diff[start] += 1
            diff[end + 1] -= 1
        acc = accumulate(diff[:-1])
        for n, d in zip(nums, acc):
            if n > d:
                return False
        return True
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.isZeroArray, ([1, 0, 1], [[0, 2]]), True),
        (solution.isZeroArray, ([4, 3, 2, 1], [[1, 3], [0, 2]]), False),
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
# [1,0,1]\n[[0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n[[1,3],[0,2]]\n
# @lcpr case=end

#
