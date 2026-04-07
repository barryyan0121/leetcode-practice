#
# @lc app=leetcode.cn id=354 lang=python3
# @lcpr version=30203
#
# [354] 俄罗斯套娃信封问题
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *
from bisect import bisect_left


# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []
        for _, h in envelopes:
            i = bisect_left(lis, h)
            if i == len(lis):
                lis.append(h)
            else:
                lis[i] = h
        return len(lis)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxEnvelopes, ([[5, 4], [6, 4], [6, 7], [2, 3]],), 3),
        (solution.maxEnvelopes, ([[1, 1], [1, 1], [1, 1]],), 1),
        (solution.maxEnvelopes, ([],), 0),
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
# [[5,4],[6,4],[6,7],[2,3]]\n
# @lcpr case=end
