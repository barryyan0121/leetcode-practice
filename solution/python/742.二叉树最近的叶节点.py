#
# @lc app=leetcode.cn id=742 lang=python3
#
# [742] 二叉树最近的叶节点
#


# @lc code=start
from collections import deque


class Solution:
    def findClosestLeaf(self, root, k: int) -> int:
        parents = {}
        target = None

        def build(node, parent=None):
            nonlocal target
            if not node:
                return
            if node.val == k:
                target = node
            parents[node] = parent
            build(node.left, node)
            build(node.right, node)

        build(root)
        queue, seen = deque([target]), {target}
        while queue:
            leaves = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    leaves.append(node.val)
                for neighbor in (node.left, node.right, parents[node]):
                    if neighbor is not None and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            if leaves:
                return min(leaves)

if __name__ == "__main__":
    class Node:
        def __init__(self, val, left=None, right=None): self.val, self.left, self.right = val, left, right
    root = Node(1, Node(2, None, Node(3)), Node(4))
    assert Solution().findClosestLeaf(root, 2) == 3


if __name__ == "__main__":
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val, self.left, self.right = val, left, right

    root = TreeNode(1, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(2))
    assert Solution().findClosestLeaf(root, 3) == 4
