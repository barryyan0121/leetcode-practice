#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
#

import os
import sys
from typing import Optional

from common.node import TreeNode


# @lc code=start
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root if root.val or root.left or root.right else None


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.pruneTree,
            (TreeNode.create_root([1, None, 0, 0, 1]),),
            "1,null,0,null,1,null,null",
        ),
        (
            solution.pruneTree,
            (TreeNode.create_root([1, 0, 1, 0, 0, 0, 1]),),
            "1,null,1,null,1,null,null",
        ),
        (solution.pruneTree, (TreeNode.create_root([0]),), "null"),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = TreeNode.print_tree(func(*args))
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
