#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#

import os
import sys
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(limit):
            counts = defaultdict(int)
            left = result = 0
            for right, number in enumerate(nums):
                if counts[number] == 0:
                    limit -= 1
                counts[number] += 1
                while limit < 0:
                    counts[nums[left]] -= 1
                    if counts[nums[left]] == 0:
                        limit += 1
                    left += 1
                result += right - left + 1
            return result

        return at_most(k) - at_most(k - 1)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.subarraysWithKDistinct, ([1, 2, 1, 2, 3], 2), 7),
        (solution.subarraysWithKDistinct, ([1, 2, 1, 3, 4], 3), 3),
        (solution.subarraysWithKDistinct, ([1, 1, 1], 1), 6),
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
