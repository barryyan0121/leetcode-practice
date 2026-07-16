#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        difference = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob = set(bobSizes)
        for candy in aliceSizes:
            if candy - difference in bob:
                return [candy, candy - difference]
        return []


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.fairCandySwap, ([1, 1], [2, 2]), [1, 2]),
        (solution.fairCandySwap, ([1, 2], [2, 3]), [1, 2]),
        (solution.fairCandySwap, ([2], [1, 3]), [2, 3]),
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
