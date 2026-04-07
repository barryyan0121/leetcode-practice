#
# @lc app=leetcode.cn id=363 lang=python3
# @lcpr version=30203
#
# [363] 矩形区域不超过 K 的最大数值和
#

import sys
import os
from bisect import bisect_left, insort

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float("-inf")
        for left in range(n):
            row_sum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]
                prefix = [0]
                curr = 0
                best = float("-inf")
                for s in row_sum:
                    curr += s
                    idx = bisect_left(prefix, curr - k)
                    if idx < len(prefix):
                        best = max(best, curr - prefix[idx])
                    insort(prefix, curr)
                ans = max(ans, best)
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxSumSubmatrix, [[[-1, 0], [0, -2]], 0], 0),
        (solution.maxSumSubmatrix, [[[2, 2, -1]], 3], 3),
        (solution.maxSumSubmatrix, [[[1, 0, 1], [0, -2, 3]], 2], 2),
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
# [[1,0,1],[0,-2,3]]\n2\n
# @lcpr case=end

#
