from typing import List, Optional

from common.node import TreeNode


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            if node.left is not None and node.right is None:
                result.append(node.left.val)
            if node.right is not None and node.left is None:
                result.append(node.right.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    assert Solution().getLonelyNodes(root) == [4, 5]
