#
# @lc app=leetcode.cn id=220 lang=python3
# @lcpr version=30203
#
# [220] 存在重复元素 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        size = valueDiff + 1
        buckets = {}

        def get_bucket_id(x: int) -> int:
            return x // size

        for i, num in enumerate(nums):
            bid = get_bucket_id(num)
            if bid in buckets:
                return True
            if bid - 1 in buckets and abs(num - buckets[bid - 1]) <= valueDiff:
                return True
            if bid + 1 in buckets and abs(num - buckets[bid + 1]) <= valueDiff:
                return True
            buckets[bid] = num
            if i >= indexDiff:
                old_bid = get_bucket_id(nums[i - indexDiff])
                buckets.pop(old_bid, None)
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.containsNearbyAlmostDuplicate, [[1, 2, 3, 1], 3, 0], True),
        (solution.containsNearbyAlmostDuplicate, [[1, 5, 9, 1, 5, 9], 2, 3], False),
        (solution.containsNearbyAlmostDuplicate, [[1, 2], 1, 0], False),
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
# [1,2,3,1]\n3\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,5,9,1,5,9]\n2\n3\n
# @lcpr case=end

#
