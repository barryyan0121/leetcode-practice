#
# @lc app=leetcode.cn id=321 lang=python3
# @lcpr version=30203
#
# [321] 拼接最大数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums: List[int], t: int) -> List[int]:
            drop = len(nums) - t
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]

        def greater(a: List[int], i: int, b: List[int], j: int) -> bool:
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1
            return j == len(b) or (i < len(a) and a[i] > b[j])

        def merge(a: List[int], b: List[int]) -> List[int]:
            res = []
            i = j = 0
            while i < len(a) or j < len(b):
                if greater(a, i, b, j):
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            return res

        best = []
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))
        for i in range(start, end + 1):
            cand = merge(pick(nums1, i), pick(nums2, k - i))
            if cand > best:
                best = cand
        return best


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.maxNumber,
            [[3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5],
            [9, 8, 6, 5, 3],
        ),
        (solution.maxNumber, [[6, 7], [6, 0, 4], 5], [6, 7, 6, 0, 4]),
        (solution.maxNumber, [[3, 9], [8, 9], 3], [9, 8, 9]),
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
# [3,4,6,5]\n[9,1,2,5,8,3]\n5\n
# @lcpr case=end

#
