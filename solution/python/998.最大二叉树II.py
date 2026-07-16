#
# @lc app=leetcode.cn id=998 lang=python3
#
# [998] 最大二叉树 II
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        root.right = (
            self.insertIntoMaxTree(root.right, val) if root.right else TreeNode(val)
        )
        return root


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.insertIntoMaxTree,
            (TreeNode.create_root([4, 1, 3, None, None, 2]), 5),
            "5,4,1,null,null,3,2,null,null,null,null",
        ),
        (
            solution.insertIntoMaxTree,
            (TreeNode.create_root([5, 2, 4, None, 1]), 3),
            "5,2,null,1,null,null,4,null,3,null,null",
        ),
        (
            solution.insertIntoMaxTree,
            (TreeNode.create_root([5, 2, 3, None, 1]), 4),
            "5,2,null,1,null,null,4,3,null,null,null",
        ),
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
