#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = down = result = 1
        for previous, current in zip(arr, arr[1:]):
            if current > previous:
                up, down = down + 1, 1
            elif current < previous:
                up, down = 1, up + 1
            else:
                up = down = 1
            result = max(result, up, down)
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxTurbulenceSize, ([9, 4, 2, 10, 7, 8, 8, 1, 9],), 5),
        (solution.maxTurbulenceSize, ([4, 8, 12, 16],), 2),
        (solution.maxTurbulenceSize, ([100],), 1),
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
