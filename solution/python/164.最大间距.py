#
# @lc app=leetcode.cn id=164 lang=python3
# @lcpr version=30202
#
# [164] 最大间距
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0

        bucket_size = max(1, (mx - mn) // (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1
        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - mn) // bucket_size
            if buckets[idx][0] is None:
                buckets[idx][0] = buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)

        ans = 0
        prev_max = None
        for bmin, bmax in buckets:
            if bmin is None:
                continue
            if prev_max is not None:
                ans = max(ans, bmin - prev_max)
            prev_max = bmax
        return ans
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maximumGap, [[3, 6, 9, 1]], 3),
        (solution.maximumGap, [[10]], 0),
        (solution.maximumGap, [[1, 10000000]], 9999999),
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
# [3,6,9,1]\n
# @lcpr case=end

#
