#
# @lc app=leetcode.cn id=3349 lang=python3
# @lcpr version=30203
#
# [3349] 检测相邻递增子数组 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        cnt, precnt, ans = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                precnt, cnt = cnt, 1
            ans = max(ans, min(precnt, cnt))
            ans = max(ans, cnt // 2)
        return ans >= k


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.hasIncreasingSubarrays, ([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3), True),
        (solution.hasIncreasingSubarrays, ([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5), False),
        (solution.hasIncreasingSubarrays, ([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 6), False),
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
# [2,5,7,8,9,2,3,4,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,4,4,4,5,6,7]\n5\n
# @lcpr case=end

#
