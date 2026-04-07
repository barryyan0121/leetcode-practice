#
# @lc app=leetcode.cn id=435 lang=python3
# @lcpr version=30203
#
# [435] 无重叠区间
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        keep = 1
        for s, e in intervals[1:]:
            if s >= end:
                keep += 1
                end = e
        return len(intervals) - keep


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.eraseOverlapIntervals, [[[1, 2], [2, 3], [3, 4], [1, 3]]], 1),
        (solution.eraseOverlapIntervals, [[[1, 2], [1, 2], [1, 2]]], 2),
        (solution.eraseOverlapIntervals, [[[1, 2], [2, 3]]], 0),
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
# [[1,2],[2,3],[3,4],[1,3]]\n
# @lcpr case=end

#
