#
# @lc app=leetcode.cn id=510 lang=python3
# @lcpr version=30203
#
# [510] 二叉搜索树中的中序后继 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        parent: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


# @lc code=start
class Solution:
    def inorderSuccessor(self, node: "Node") -> Optional["Node"]:
        if node is None:
            return None
        if node.right is not None:
            cur = node.right
            while cur.left is not None:
                cur = cur.left
            return cur

        cur = node
        while cur.parent is not None and cur.parent.right is cur:
            cur = cur.parent
        return cur.parent


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build_tree() -> Dict[int, Node]:
        nodes = {value: Node(value) for value in [1, 2, 3, 4, 5, 6, 7, 8, 9]}
        nodes[6].left = nodes[3]
        nodes[6].right = nodes[8]
        nodes[3].parent = nodes[6]
        nodes[8].parent = nodes[6]

        nodes[3].left = nodes[1]
        nodes[3].right = nodes[4]
        nodes[1].parent = nodes[3]
        nodes[4].parent = nodes[3]

        nodes[1].right = nodes[2]
        nodes[2].parent = nodes[1]

        nodes[8].left = nodes[7]
        nodes[8].right = nodes[9]
        nodes[7].parent = nodes[8]
        nodes[9].parent = nodes[8]
        return nodes

    tree = build_tree()
    test_cases = [
        (solution.inorderSuccessor, (tree[1],), 2),
        (solution.inorderSuccessor, (tree[2],), 3),
        (solution.inorderSuccessor, (tree[4],), 6),
        (solution.inorderSuccessor, (tree[7],), 8),
        (solution.inorderSuccessor, (tree[9],), None),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            result_val = result.val if result else None
            assert result_val == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result_val}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result_val}"
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
# [6,3,8,1,4,7,9,null,2]\n
# @lcpr case=end
#
