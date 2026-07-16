#
# @lc app=leetcode.cn id=995 lang=python3
#
# [995] K 连续位的最小翻转次数
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        changes = [0] * (len(nums) + 1)
        flipped = result = 0
        for index, number in enumerate(nums):
            flipped ^= changes[index]
            if number == flipped:
                if index + k > len(nums):
                    return -1
                result += 1
                flipped ^= 1
                changes[index + k] ^= 1
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minKBitFlips, ([0, 1, 0], 1), 2),
        (solution.minKBitFlips, ([1, 1, 0], 2), -1),
        (solution.minKBitFlips, ([0, 0, 0, 1, 0, 1, 1, 0], 3), 3),
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
