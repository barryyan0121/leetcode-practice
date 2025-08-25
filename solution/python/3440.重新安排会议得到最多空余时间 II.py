#
# @lc app=leetcode.cn id=3440 lang=python3
# @lcpr version=30202
#
# [3440] 重新安排会议得到最多空余时间 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        q = [False] * n
        t1 = 0
        t2 = 0
        for i in range(n):
            if endTime[i] - startTime[i] <= t1:
                q[i] = True
            t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i - 1]))

            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                q[n - i - 1] = True
            t2 = max(
                t2, (eventTime if i == 0 else startTime[n - i]) - endTime[n - i - 1]
            )

        res = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            if q[i]:
                res = max(res, right - left)
            else:
                res = max(res, right - left - (endTime[i] - startTime[i]))
        return res
        # @lc code=end


if __name__ == '__main__':
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxFreeTime, (5, [1, 3], [2, 5]), 2),
        (solution.maxFreeTime, (10, [0, 7, 9], [1, 8, 10]), 7),
        (solution.maxFreeTime, (10, [0, 3, 7, 9], [1, 4, 8, 10]), 6),
        (solution.maxFreeTime, (5, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]), 0),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

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
# 5\n[1,3]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[0,7,9]\n[1,8,10]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[0,3,7,9]\n[1,4,8,10]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[0,1,2,3,4]\n[1,2,3,4,5]\n
# @lcpr case=end

#
