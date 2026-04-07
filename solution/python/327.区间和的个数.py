#
# @lc app=leetcode.cn id=327 lang=python3
# @lcpr version=30203
#
# [327] 区间和的个数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def sort_count(arr: List[int]) -> Tuple[List[int], int]:
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, c1 = sort_count(arr[:mid])
            right, c2 = sort_count(arr[mid:])
            count = c1 + c2
            j = k = t = 0
            merged = []
            for x in left:
                while k < len(right) and right[k] - x < lower:
                    k += 1
                while j < len(right) and right[j] - x <= upper:
                    j += 1
                count += j - k
            i = p = 0
            while i < len(left) and p < len(right):
                if left[i] <= right[p]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[p])
                    p += 1
            merged.extend(left[i:])
            merged.extend(right[p:])
            return merged, count

        return sort_count(prefix)[1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.countRangeSum, [[-2, 5, -1], -2, 2], 3),
        (solution.countRangeSum, [[0], 0, 0], 1),
        (solution.countRangeSum, [[1, -1], 0, 0], 1),
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
# [-2,5,-1]\n-2\n2\n
# @lcpr case=end

#
