#
# @lc app=leetcode.cn id=311 lang=python3
# @lcpr version=30203
#
# [311] 稀疏矩阵的乘法
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def multiply(
        self, mat1: List[List[int]], mat2: List[List[int]]
    ) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(k):
                if mat1[i][j] == 0:
                    continue
                for col in range(n):
                    if mat2[j][col] != 0:
                        result[i][col] += mat1[i][j] * mat2[j][col]

        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.multiply,
            (
                [[1, 0, 0], [-1, 0, 3]],
                [[7, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
            [[7, 0, 0], [-7, 0, 3]],
        ),
        (
            solution.multiply,
            (
                [[0]],
                [[0]],
            ),
            [[0]],
        ),
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
# [[1,0,0],[-1,0,3]]\n[[7,0,0],[0,0,0],[0,0,1]]\n
# @lcpr case=end
