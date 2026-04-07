#
# @lc app=leetcode.cn id=436 lang=python3
# @lcpr version=30203
#
# [436] 寻找右区间
#

import sys
import os
from bisect import bisect_left

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))
        xs = [x for x, _ in starts]
        res = []
        for start, end in intervals:
            idx = bisect_left(xs, end)
            res.append(starts[idx][1] if idx < len(starts) else -1)
        return res


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findRightInterval, [[[1, 2]]], [-1]),
        (solution.findRightInterval, [[[3, 4], [2, 3], [1, 2]]], [-1, 0, 1]),
        (solution.findRightInterval, [[[1, 4], [2, 3], [3, 4]]], [-1, 2, -1]),
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
# [[1,2]]\n
# @lcpr case=end

#
