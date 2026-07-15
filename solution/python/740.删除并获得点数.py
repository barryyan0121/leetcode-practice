#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#

import os
import sys
from collections import Counter
from typing import *


# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = Counter(nums)
        take = skip = 0
        previous = -1
        for number in sorted(points):
            gain = number * points[number]
            if number == previous + 1:
                take, skip = skip + gain, max(take, skip)
            else:
                best = max(take, skip)
                take, skip = best + gain, best
            previous = number
        return max(take, skip)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.deleteAndEarn, ([3, 4, 2],), 6),
        (solution.deleteAndEarn, ([2, 2, 3, 3, 3, 4],), 9),
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
