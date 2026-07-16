#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        index = len(num) - 1
        while index >= 0 or k:
            if index >= 0:
                k += num[index]
                index -= 1
            result.append(k % 10)
            k //= 10
        return result[::-1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.addToArrayForm, ([1, 2, 0, 0], 34), [1, 2, 3, 4]),
        (solution.addToArrayForm, ([2, 7, 4], 181), [4, 5, 5]),
        (solution.addToArrayForm, ([2, 1, 5], 806), [1, 0, 2, 1]),
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
