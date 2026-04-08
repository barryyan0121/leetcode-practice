#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(int(time[:2]) * 60 + int(time[3:]) for time in timePoints)
        minutes.append(minutes[0] + 24 * 60)
        return min(b - a for a, b in zip(minutes, minutes[1:]))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findMinDifference, (["23:59", "00:00"],), 1),
        (solution.findMinDifference, (["00:00", "23:59", "00:00"],), 0),
        (solution.findMinDifference, (["01:01", "02:01", "03:00"],), 59),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# ["23:59","00:00"]\n
# @lcpr case=end
#
