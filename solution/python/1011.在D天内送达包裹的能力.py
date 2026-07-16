#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def required(capacity):
            used = 1
            load = 0
            for weight in weights:
                if load + weight > capacity:
                    used += 1
                    load = 0
                load += weight
            return used

        left, right = max(weights), sum(weights)
        while left < right:
            middle = (left + right) // 2
            if required(middle) <= days:
                right = middle
            else:
                left = middle + 1
        return left


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.shipWithinDays, ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15),
        (solution.shipWithinDays, ([3, 2, 2, 4, 1, 4], 3), 6),
        (solution.shipWithinDays, ([1, 2, 3, 1, 1], 4), 3),
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
