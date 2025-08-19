#
# @lc app=leetcode.cn id=218 lang=python3
# @lcpr version=30202
#
# [218] 天际线问题
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import List
from bisect import bisect_left, bisect_right


# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0:
            return []

        buildings.sort(key=lambda v: v[2])
        pos, height = [0], [0]
        for left, right, h in buildings:
            i = bisect_left(pos, left)
            j = bisect_right(pos, right)
            height[i:j] = [h, height[j - 1]]
            pos[i:j] = [left, right]
        print(height, pos)
        res = []
        prev = 0
        for v, h in zip(pos, height):
            if h != prev:
                res.append([v, h])
                prev = h

        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.getSkyline,
            [[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]],
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
        ),
        (solution.getSkyline, [[[0, 2, 3], [2, 5, 3]]], [[0, 3], [5, 0]]),
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
# [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,2,3],[2,5,3]]\n
# @lcpr case=end

#
