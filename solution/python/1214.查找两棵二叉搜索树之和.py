import os
import sys
from typing import Optional, Set

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


class Solution:
    def twoSumBSTs(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int
    ) -> bool:
        values: Set[int] = set()

        def collect(node: Optional[TreeNode]) -> None:
            if node:
                values.add(node.val)
                collect(node.left)
                collect(node.right)

        def find(node: Optional[TreeNode]) -> bool:
            return bool(node) and (
                target - node.val in values or find(node.left) or find(node.right)
            )

        collect(root1)
        return find(root2)


if __name__ == "__main__":
    test_cases = [
        (TreeNode.create_root([2, 1, 4]), TreeNode.create_root([1, 0, 3]), 5, True)
    ]
    for _, (root1, root2, target, expected) in enumerate(test_cases):
        assert Solution().twoSumBSTs(root1, root2, target) == expected
