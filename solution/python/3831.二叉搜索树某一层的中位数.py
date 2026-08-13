from collections import deque
from typing import Optional


class Solution:
    def levelMedian(self, root: Optional["TreeNode"], level: int) -> int:
        queue = deque([root])
        for _ in range(level):
            queue = deque(
                child for node in queue for child in (node.left, node.right) if child
            )
            if not queue:
                return -1
        values = [node.val for node in queue]
        return values[len(values) // 2]


if __name__ == "__main__":
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8))
    assert Solution().levelMedian(root, 0) == 5
    assert Solution().levelMedian(root, 1) == 8
    assert Solution().levelMedian(root, 2) == 4
