#
# @lc app=leetcode.cn id=3356 lang=python3
# @lcpr version=30202
#
# [3356] 零数组变换 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        deltaArray = [0] * (n + 1)
        operations = 0
        k = 0
        for i in range(n):
            num = nums[i]
            operations += deltaArray[i]
            while k < len(queries) and operations < num:
                left, right, value = queries[k]
                deltaArray[left] += value
                deltaArray[right + 1] -= value
                if left <= i <= right:
                    operations += value
                k += 1
            if operations < num:
                return -1
        return k
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.minZeroArray, ([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]), 2),
        (solution.minZeroArray, ([4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]]), -1),
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
# [2,0,2]\n[[0,2,1],[0,2,1],[1,1,3]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n[[1,3,2],[0,2,1]]\n
# @lcpr case=end

#
