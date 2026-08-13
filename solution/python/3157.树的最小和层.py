"""3157. 树的最小和层"""

from collections import deque
from math import inf
from typing import Optional


class Solution:
    def minimumLevel(self, root: Optional["TreeNode"]) -> int:
        q = deque([root])
        ans = 0
        level, s = 1, inf
        while q:
            total = 0
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > total:
                s = total
                ans = level
            level += 1
        return ans


if __name__ == "__main__":

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val, self.left, self.right = val, left, right

    f = Solution().minimumLevel
    assert f(TreeNode(50, TreeNode(6), TreeNode(2))) == 2
    assert f(TreeNode(5, None, TreeNode(5, None, TreeNode(5)))) == 1
