from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        queue = deque([root])
        while queue:
            size = len(queue)
            for index in range(size):
                node = queue.popleft()
                if node is u:
                    return queue[0] if index + 1 < size else None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


if __name__ == "__main__":
    test_cases = [(TreeNode(1, TreeNode(2), TreeNode(3)),)]
    for _, (root,) in enumerate(test_cases):
        assert Solution().findNearestRightNode(root, root.left) is root.right
