#
# @lc app=leetcode.cn id=1504 lang=python3
# @lcpr version=30202
#
# [1504] 统计全 1 子矩形
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0

        # 第一行：高度就是元素值本身
        # 从第二行开始，原地更新高度信息
        for i in range(m):
            for j in range(n):
                if i > 0 and mat[i][j] == 1:
                    mat[i][j] = mat[i - 1][j] + 1  # 更新为高度值

                if mat[i][j] > 0:  # 当前高度大于0
                    min_height = mat[i][j]
                    # 向左遍历，计算以(i,j)为右下角的所有矩形
                    for k in range(j, -1, -1):
                        if mat[i][k] == 0:
                            break
                        min_height = min(min_height, mat[i][k])
                        ans += min_height

        return ans

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.numSubmat, ([[1, 0, 1], [1, 1, 0], [1, 1, 0]],), 13),
        (solution.numSubmat, ([[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]],), 24),
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
# [[1,0,1],[1,1,0],[1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,1,0],[0,1,1,1],[1,1,1,0]]\n
# @lcpr case=end

#
