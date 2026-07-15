#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(maximum: int) -> int:
            answer = length = 0
            for number in nums:
                length = length + 1 if number <= maximum else 0
                answer += length
            return answer

        return count(right) - count(left - 1)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numSubarrayBoundedMax, ([2, 1, 4, 3], 2, 3), 3),
        (solution.numSubarrayBoundedMax, ([2, 9, 2, 5, 6], 2, 8), 7),
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
