#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixes = Counter({0: 1})
        total = answer = 0
        for number in nums:
            total += number
            answer += prefixes[total - goal]
            prefixes[total] += 1
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numSubarraysWithSum, ([1, 0, 1, 0, 1], 2), 4),
        (solution.numSubarraysWithSum, ([0, 0, 0, 0, 0], 0), 15),
        (solution.numSubarraysWithSum, ([1, 1, 1], 2), 2),
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
