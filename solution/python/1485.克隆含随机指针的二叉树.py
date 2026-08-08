from typing import Optional


class Node:
    def __init__(self, val: int = 0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class NodeCopy(Node):
    pass


class Solution:
    def copyRandomBinaryTree(self, root: "Optional[Node]") -> "Optional[NodeCopy]":
        if not root:
            return None
        copies = {root: NodeCopy(root.val)}
        stack = [root]
        while stack:
            node = stack.pop()
            for attr in ("left", "right", "random"):
                child = getattr(node, attr)
                if child and child not in copies:
                    copies[child] = NodeCopy(child.val)
                    stack.append(child)
                setattr(copies[node], attr, copies.get(child))
        return copies[root]


if __name__ == "__main__":
    test_cases = [(Node(1),)]
    for _, (root,) in enumerate(test_cases):
        root.left = Node(2)
        root.right = Node(3)
        root.random = root.right
        root.left.random = root
        result = Solution().copyRandomBinaryTree(root)
        assert result is not root
        assert result.val == 1 and result.left.val == 2 and result.right.val == 3
        assert result.random is result.right and result.left.random is result
