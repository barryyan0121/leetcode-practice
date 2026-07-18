#
# @lc app=leetcode.cn id=1031 lang=python3
#
# [1031] 两个非重叠子数组的最大和
#

import os
import sys
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0, *accumulate(nums)]

        def best(left_length, right_length):
            result = left_best = 0
            for end in range(left_length + right_length, len(nums) + 1):
                left_best = max(
                    left_best,
                    prefix[end - right_length]
                    - prefix[end - right_length - left_length],
                )
                right_sum = prefix[end] - prefix[end - right_length]
                result = max(result, left_best + right_sum)
            return result

        return max(best(firstLen, secondLen), best(secondLen, firstLen))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxSumTwoNoOverlap, ([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2), 20),
        (solution.maxSumTwoNoOverlap, ([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2), 29),
        (solution.maxSumTwoNoOverlap, ([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3), 31),
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
