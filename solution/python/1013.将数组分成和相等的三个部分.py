#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3:
            return False
        target = total // 3
        prefix = 0
        first_part = False
        for number in arr[:-1]:
            prefix += number
            if first_part and prefix == 2 * target:
                return True
            if prefix == target:
                first_part = True
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.canThreePartsEqualSum, ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1],), True),
        (solution.canThreePartsEqualSum, ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1],), False),
        (solution.canThreePartsEqualSum, ([3, 3, 6, 5, -2, 2, 5, 1, -9, 4],), True),
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
