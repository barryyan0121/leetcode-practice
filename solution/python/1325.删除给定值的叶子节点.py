# @lc app=leetcode.cn id=1325 lang=python3

from typing import Optional

from common.node import TreeNode


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        return None if root.val == target and not root.left and not root.right else root


if __name__ == "__main__":
    test_cases = [
        (Solution().removeLeafNodes, (TreeNode.create_root([1, 2, 2]), 2), 1),
        (Solution().removeLeafNodes, (TreeNode.create_root([1, 1, 1]), 1), None),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        actual = func(*args)
        if expected is None:
            assert actual is None
        else:
            assert (
                actual.val == expected and actual.left is None and actual.right is None
            )
    print('第 1325 题 "删除给定值的叶子节点" 所有测试用例通过')
