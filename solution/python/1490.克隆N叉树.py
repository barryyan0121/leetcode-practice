from typing import Optional


class Node:
    def __init__(self, val: int = 0, children=None):
        self.val = val
        self.children = children or []


class Solution:
    def cloneTree(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None
        copies = {root: Node(root.val)}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in node.children:
                if child not in copies:
                    copies[child] = Node(child.val)
                    stack.append(child)
                copies[node].children.append(copies[child])
        return copies[root]


if __name__ == "__main__":
    test_cases = [(Node(1, [Node(2), Node(3)]),)]
    for _, (root,) in enumerate(test_cases):
        root.children[0].children.append(Node(4))
        result = Solution().cloneTree(root)
        assert result is not root
        assert [child.val for child in result.children] == [2, 3]
        assert result.children[0] is not root.children[0]
        assert result.children[0].children[0].val == 4
