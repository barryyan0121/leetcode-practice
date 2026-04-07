#
# @lc app=leetcode.cn id=373 lang=python3
# @lcpr version=30203
#
# [373] 查找和最小的 K 对数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from heapq import heappop, heappush
from common.node import *


# @lc code=start
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        for i in range(min(k, len(nums1))):
            heappush(heap, (nums1[i] + nums2[0], i, 0))

        res = []
        while heap and len(res) < k:
            _, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.kSmallestPairs, [[1, 7, 11], [2, 4, 6], 3], [[1, 2], [1, 4], [1, 6]]),
        (solution.kSmallestPairs, [[1, 1, 2], [1, 2, 3], 2], [[1, 1], [1, 1]]),
        (solution.kSmallestPairs, [[], [1, 2], 3], []),
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
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

#
