#
# @lc app=leetcode.cn id=572 lang=python3
# @lcpr version=30203
#
# [572] 另一棵树的子树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if a is None or b is None:
                return a is b
            return (
                a.val == b.val
                and same_tree(a.left, b.left)
                and same_tree(a.right, b.right)
            )

        if subRoot is None:
            return True
        if root is None:
            return False
        return (
            same_tree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values:
            return None
        nodes = [None if value is None else TreeNode(value) for value in values]
        children = nodes[::-1]
        root = children.pop()
        for node in nodes:
            if node is None:
                continue
            if children:
                node.left = children.pop()
            if children:
                node.right = children.pop()
        return root

    test_cases = [
        (
            solution.isSubtree,
            (build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])),
            True,
        ),
        (
            solution.isSubtree,
            (
                build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]),
                build_tree([4, 1, 2]),
            ),
            False,
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
# root = TreeNode(root of the tree), subRoot = TreeNode(root of the subtree)\n
# @lcpr case=end
