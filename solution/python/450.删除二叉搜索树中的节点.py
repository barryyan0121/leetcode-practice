#
# @lc app=leetcode.cn id=450 lang=python3
# @lcpr version=30203
#
# [450] 删除二叉搜索树中的节点
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            successor = root.right
            while successor.left is not None:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.deleteNode,
            (TreeNode.create_root([5, 3, 6, 2, 4, None, 7]), 3),
            "5,4,2,null,null,null,6,null,7,null,null",
        ),
        (
            solution.deleteNode,
            (TreeNode.create_root([5, 3, 6, 2, 4, None, 7]), 0),
            "5,3,2,null,null,4,null,null,6,null,7,null,null",
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            printed = TreeNode.print_tree(result)
            assert printed == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {printed}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {printed}"
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
# [5,3,6,2,4,null,7]\n3\n
# @lcpr case=end
