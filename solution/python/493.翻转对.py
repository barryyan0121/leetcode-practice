#
# @lc app=leetcode.cn id=493 lang=python3
# @lcpr version=30203
#
# [493] 翻转对
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort_count(arr: List[int]) -> int:
            n = len(arr)
            if n <= 1:
                return 0
            mid = n // 2
            left = arr[:mid]
            right = arr[mid:]
            count = sort_count(left) + sort_count(right)
            j = 0
            for x in left:
                while j < len(right) and x > 2 * right[j]:
                    j += 1
                count += j
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
            return count

        return sort_count(nums[:])


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.reversePairs, ([1, 3, 2, 3, 1],), 2),
        (solution.reversePairs, ([2, 4, 3, 5, 1],), 3),
        (solution.reversePairs, ([5, 4, 3, 2, 1],), 4),
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
# [1,3,2,3,1]\n
# @lcpr case=end

#
