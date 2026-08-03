# @lc app=leetcode.cn id=1315 lang=python3

from typing import Optional

from common.node import TreeNode


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(
            node: Optional[TreeNode], parent: Optional[int], grandparent: Optional[int]
        ) -> int:
            if not node:
                return 0
            total = node.val if grandparent is not None and grandparent % 2 == 0 else 0
            return (
                total
                + dfs(node.left, node.val, parent)
                + dfs(node.right, node.val, parent)
            )

        return dfs(root, None, None)


if __name__ == "__main__":
    test_cases = [
        (
            Solution().sumEvenGrandparent,
            (
                TreeNode.create_root(
                    [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
                ),
            ),
            18,
        ),
        (Solution().sumEvenGrandparent, (TreeNode.create_root([1]),), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1315 题 "祖父节点值为偶数的节点和" 所有测试用例通过')
