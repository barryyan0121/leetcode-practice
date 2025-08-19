#
# @lc app=leetcode.cn id=2294 lang=python3
# @lcpr version=30202
#
# [2294] 划分数组使最大差为 K
#

import sys
import os
from math import inf

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        mn = -inf
        for i in nums:
            if i - mn > k:
                res += 1
                mn = i
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.partitionArray, ([3, 6, 1, 2, 5], 2), 2),
        (solution.partitionArray, ([1, 2, 3], 1), 2),
        (solution.partitionArray, ([2, 2, 4, 5], 0), 3),
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
# [3,6,1,2,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,4,5]\n0\n
# @lcpr case=end

#
