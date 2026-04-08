#
# @lc app=leetcode.cn id=532 lang=python3
# @lcpr version=30203
#
# [532] 数组中的 k-diff 数对
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        counts = Counter(nums)
        if k == 0:
            return sum(freq > 1 for freq in counts.values())

        unique = sorted(counts)
        left = 0
        right = 1
        ans = 0
        while left < len(unique) and right < len(unique):
            diff = unique[right] - unique[left]
            if left == right or diff < k:
                right += 1
            elif diff > k:
                left += 1
            else:
                ans += 1
                left += 1
                right += 1
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findPairs, ([3, 1, 4, 1, 5], 2), 2),
        (solution.findPairs, ([1, 2, 3, 4, 5], 1), 4),
        (solution.findPairs, ([1, 3, 1, 5, 4], 0), 1),
        (solution.findPairs, ([1, 2, 3, 4, 5], -1), 0),
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
# [3,1,4,1,5]\n2\n
# @lcpr case=end
#
