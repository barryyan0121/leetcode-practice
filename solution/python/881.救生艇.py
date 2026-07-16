#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        light, heavy = 0, len(people) - 1
        boats = 0
        while light <= heavy:
            if people[light] + people[heavy] <= limit:
                light += 1
            heavy -= 1
            boats += 1
        return boats


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numRescueBoats, ([1, 2], 3), 1),
        (solution.numRescueBoats, ([3, 2, 2, 1], 3), 3),
        (solution.numRescueBoats, ([3, 5, 3, 4], 5), 4),
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
