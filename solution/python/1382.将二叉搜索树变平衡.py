# @lc app=leetcode.cn id=1382 lang=python3
from typing import Optional
from common.node import TreeNode


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def inorder(node):
            if node:
                inorder(node.left)
                values.append(node.val)
                inorder(node.right)

        def build(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            node = TreeNode(values[middle])
            node.left, node.right = build(left, middle - 1), build(middle + 1, right)
            return node

        inorder(root)
        return build(0, len(values) - 1)


if __name__ == "__main__":
    test_cases = ["balance"]
    for _, _case in enumerate(test_cases):
        pass
    result = Solution().balanceBST(TreeNode.create_root([1, None, 2, None, 3, None, 4]))
    assert result.val == 2 and result.left.val == 1 and result.right.val == 3
    print('第 1382 题 "将二叉搜索树变平衡" 所有测试用例通过')
