#
# @lc app=leetcode.cn id=427 lang=python3
# @lcpr version=30203
#
# [427] 建立四叉树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class QuadTreeNode:
    def __init__(
        self,
        val: bool,
        isLeaf: bool,
        topLeft: Optional["QuadTreeNode"] = None,
        topRight: Optional["QuadTreeNode"] = None,
        bottomLeft: Optional["QuadTreeNode"] = None,
        bottomRight: Optional["QuadTreeNode"] = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# @lc code=start
class Solution:
    def construct(self, grid: List[List[int]]) -> "QuadTreeNode":
        n = len(grid)

        def build(r0: int, c0: int, size: int) -> QuadTreeNode:
            first = grid[r0][c0]
            same = True
            for i in range(r0, r0 + size):
                for j in range(c0, c0 + size):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break
            if same:
                return QuadTreeNode(bool(first), True)
            half = size // 2
            return QuadTreeNode(
                True,
                False,
                build(r0, c0, half),
                build(r0, c0 + half, half),
                build(r0 + half, c0, half),
                build(r0 + half, c0 + half, half),
            )

        return build(0, 0, n)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def count_nodes(root: Optional[QuadTreeNode]) -> int:
        if not root:
            return 0
        return 1 + count_nodes(root.topLeft) + count_nodes(root.topRight) + count_nodes(root.bottomLeft) + count_nodes(root.bottomRight)

    # 测试用例 (func, args, result)
    test_cases = [
        (count_nodes, [solution.construct([[0, 1], [1, 0]])], 5),
        (count_nodes, [solution.construct([[1, 1], [1, 1]])], 1),
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
# [[0,1],[1,0]]\n
# @lcpr case=end

#
