#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 在长度 2N 的数组中找出重复 N 次的元素
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for number in nums:
            if number in seen:
                return number
            seen.add(number)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.repeatedNTimes, ([1, 2, 3, 3],), 3),
        (solution.repeatedNTimes, ([2, 1, 2, 5, 3, 2],), 2),
        (solution.repeatedNTimes, ([5, 1, 5, 2, 5, 3, 5, 4],), 5),
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
