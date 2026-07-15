#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            middle = (left + right) // 2
            if arr[middle] < arr[middle + 1]:
                left = middle + 1
            else:
                right = middle
        return left


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.peakIndexInMountainArray, ([0, 1, 0],), 1),
        (solution.peakIndexInMountainArray, ([0, 2, 1, 0],), 1),
        (solution.peakIndexInMountainArray, ([0, 10, 5, 2],), 1),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
