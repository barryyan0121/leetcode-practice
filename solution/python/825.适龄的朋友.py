#
# @lc app=leetcode.cn id=825 lang=python3
#
# [825] 适龄的朋友
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = Counter(ages)
        return sum(
            first_count * (second_count - (first_age == second_age))
            for first_age, first_count in counts.items()
            for second_age, second_count in counts.items()
            if 2 * second_age > first_age + 14 and second_age <= first_age
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numFriendRequests, ([16, 16],), 2),
        (solution.numFriendRequests, ([16, 17, 18],), 2),
        (solution.numFriendRequests, ([20, 30, 100, 110, 120],), 3),
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
