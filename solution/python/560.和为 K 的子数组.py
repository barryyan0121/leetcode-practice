#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30203
#
# [560] 和为 K 的子数组
#

import sys
import os
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = defaultdict(int)
        count[0] = 1
        ans = 0
        for num in nums:
            prefix += num
            ans += count[prefix - k]
            count[prefix] += 1
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.subarraySum, ([1, 1, 1], 2), 2),
        (solution.subarraySum, ([1, 2, 3], 3), 2),
        (solution.subarraySum, ([1], 0), 0),
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
# [1,1,1]\n2\n
# @lcpr case=end
#
