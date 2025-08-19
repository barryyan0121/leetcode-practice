#
# @lc app=leetcode.cn id=2966 lang=python3
# @lcpr version=30202
#
# [2966] 划分数组并满足最大差限制
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] <= k:
                res.append(nums[i : i + 3])
            else:
                return []
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.divideArray,
            ([1, 3, 4, 8, 7, 9, 3, 5, 1], 2),
            [[1, 1, 3], [3, 4, 5], [7, 8, 9]],
        ),
        (solution.divideArray, ([2, 4, 2, 2, 5, 2], 2), []),
        (
            solution.divideArray,
            ([4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14),
            [[2, 2, 2], [4, 5, 5], [5, 5, 7], [7, 8, 8], [9, 9, 10], [11, 12, 12]],
        ),
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
# [1,3,4,8,7,9,3,5,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,4,2,2,5,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]\n14\n
# @lcpr case=end

#
