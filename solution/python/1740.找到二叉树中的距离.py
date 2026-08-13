from typing import Optional

from common.node import TreeNode


class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def path(node: Optional[TreeNode], target: int) -> list[int] | None:
            if node is None:
                return None
            if node.val == target:
                return [node.val]
            for child in (node.left, node.right):
                found = path(child, target)
                if found is not None:
                    return [node.val] + found
            return None

        path_p = path(root, p)
        path_q = path(root, q)
        common = 0
        while common < len(path_p) and common < len(path_q):
            if path_p[common] != path_q[common]:
                break
            common += 1
        return len(path_p) + len(path_q) - 2 * common


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    assert Solution().findDistance(root, 5, 1) == 2
