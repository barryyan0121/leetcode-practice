#
# @lc app=leetcode.cn id=910 lang=python3
#
# [910] 最小差值 II
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = nums[-1] - nums[0]
        for index in range(len(nums) - 1):
            high = max(nums[index] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[index + 1] - k)
            answer = min(answer, high - low)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.smallestRangeII, ([1], 0), 0),
        (solution.smallestRangeII, ([0, 10], 2), 6),
        (solution.smallestRangeII, ([1, 3, 6], 3), 3),
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
