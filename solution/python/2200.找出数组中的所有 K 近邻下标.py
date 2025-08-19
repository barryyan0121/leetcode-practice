#
# @lc app=leetcode.cn id=2200 lang=python3
# @lcpr version=30202
#
# [2200] 找出数组中的所有 K 近邻下标
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_idx = []
        for i, num in enumerate(nums):
            if num == key:
                key_idx.append(i)

        result = []
        for i in range(len(nums)):
            for j in key_idx:
                if abs(i - j) <= k:
                    result.append(i)
                    break
        return result
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findKDistantIndices,
            ([3, 4, 9, 1, 3, 9, 5], 9, 1),
            [1, 2, 3, 4, 5, 6],
        ),
        (solution.findKDistantIndices, ([2, 2, 2, 2, 2], 2, 2), [0, 1, 2, 3, 4]),
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
# [3,4,9,1,3,9,5]\n9\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n2\n2\n
# @lcpr case=end

#
