#
# @lc app=leetcode.cn id=378 lang=python3
# @lcpr version=30203
#
# [378] 有序矩阵中第 K 小的元素
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_leq(x: int) -> int:
            row, col = n - 1, 0
            cnt = 0
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    cnt += row + 1
                    col += 1
                else:
                    row -= 1
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if count_leq(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.kthSmallest, [[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8], 13),
        (solution.kthSmallest, [[[1, 2], [1, 3]], 2], 1),
        (solution.kthSmallest, [[[1, 2], [3, 4]], 3], 3),
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
# [[1,5,9],[10,11,13],[12,13,15]]\n8\n
# @lcpr case=end

#
