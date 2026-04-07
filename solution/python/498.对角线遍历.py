#
# @lc app=leetcode.cn id=498 lang=python3
# @lcpr version=30203
#
# [498] 对角线遍历
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        for s in range(m + n - 1):
            cur = []
            x = 0 if s < n else s - n + 1
            y = s if s < n else n - 1
            while x < m and y >= 0:
                cur.append(mat[x][y])
                x += 1
                y -= 1
            if s % 2 == 0:
                ans.extend(cur[::-1])
            else:
                ans.extend(cur)
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findDiagonalOrder,
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
            [1, 2, 4, 7, 5, 3, 6, 8, 9],
        ),
        (
            solution.findDiagonalOrder,
            ([[1, 2], [3, 4]],),
            [1, 2, 3, 4],
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
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

#
