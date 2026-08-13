from collections import deque
from typing import Optional


class Solution:
    def levelMedian(self, root: Optional["TreeNode"], level: int) -> int:
        queue = deque([root])
        for _ in range(level):
            queue = deque(child for node in queue for child in (node.left, node.right) if child)
            if not queue:
                return -1
        values = [node.val for node in queue]
        return values[len(values) // 2]
