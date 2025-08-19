#
# @lc app=leetcode.cn id=1751 lang=python3
# @lcpr version=30202
#
# [1751] 最多可以参加的会议数目 II
#

import sys
import os
from bisect import bisect_left

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i, (start, end, val) in enumerate(events):
            p = bisect_left(events, start, hi=n - 1, key=lambda e: e[1])
            for j in range(1, k + 1):
                dp[i + 1][j] = max(dp[i][j], dp[p][j - 1] + events[i][2])

        return dp[n][k]
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxValue, ([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2), 7),
        (solution.maxValue, ([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2), 10),
        (solution.maxValue, ([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3), 9),
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
# [[1,2,4],[3,4,3],[2,3,1]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,4],[3,4,3],[2,3,10]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]\n3\n
# @lcpr case=end

#
