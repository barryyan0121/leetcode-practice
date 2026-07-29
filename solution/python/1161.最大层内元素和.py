from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        answer = level = 1
        maximum = root.val
        while queue:
            total = sum(node.val for node in queue)
            if total > maximum:
                maximum, answer = total, level
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return answer


if __name__ == "__main__":
    test_cases = [(TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0)), 2)]
    for _, (root, expected) in enumerate(test_cases):
        assert Solution().maxLevelSum(root) == expected
