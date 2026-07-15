#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            elif ten:
                five -= 1
                ten -= 1
            else:
                five -= 3
            if five < 0:
                return False
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.lemonadeChange, ([5, 5, 5, 10, 20],), True),
        (solution.lemonadeChange, ([5, 5, 10, 10, 20],), False),
        (solution.lemonadeChange, ([10],), False),
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
