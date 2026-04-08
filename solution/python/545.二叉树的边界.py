#
# @lc app=leetcode.cn id=545 lang=python3
# @lcpr version=30203
#
# [545] 二叉树的边界
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        res = [root.val]

        node = root.left
        while node:
            if not is_leaf(node):
                res.append(node.val)
            node = node.left if node.left else node.right

        def add_leaves(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if is_leaf(node):
                res.append(node.val)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        add_leaves(root.left)
        add_leaves(root.right)

        right = []
        node = root.right
        while node:
            if not is_leaf(node):
                right.append(node.val)
            node = node.right if node.right else node.left

        res.extend(reversed(right))
        return res


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.boundaryOfBinaryTree,
            (TreeNode.create_root([1, None, 2, 3, 4]),),
            [1, 3, 4, 2],
        ),
        (
            solution.boundaryOfBinaryTree,
            (TreeNode.create_root([1, 2, 3, 4, 5, 6, 7]),),
            [1, 2, 4, 5, 6, 7, 3],
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
# [1,null,2,3,4]\n
# @lcpr case=end
#
