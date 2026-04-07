#
# @lc app=leetcode.cn id=261 lang=python3
# @lcpr version=30203
#
# [261] 以图判树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            parent[root_a] = root_b

        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.validTree, (5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True),
        (solution.validTree, (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False),
        (solution.validTree, (4, [[0, 1], [2, 3]]), False),
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
# 5\n[[0,1],[0,2],[0,3],[1,4]]\n
# @lcpr case=end
