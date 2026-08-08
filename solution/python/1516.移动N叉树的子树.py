class Node:
    def __init__(self, val: int, children=None):
        self.val = val
        self.children = children or []


class Solution:
    def moveSubTree(self, root: Node, p: Node, q: Node) -> Node:
        parent = {root: None}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in node.children:
                parent[child] = node
                stack.append(child)

        if parent[p] is q:
            return root
        if parent[q] is not None and self._is_descendant(p, q):
            parent[q].children.remove(q)
            if parent[p] is None:
                root = q
            else:
                siblings = parent[p].children
                siblings[siblings.index(p)] = q
            q.children.append(p)
        else:
            parent[p].children.remove(p)
            q.children.append(p)
        return root

    def _is_descendant(self, root: Node, target: Node) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if node is target:
                return True
            stack.extend(node.children)
        return False


if __name__ == "__main__":
    test_cases = [(Node(1, [Node(2), Node(3)]),)]
    for _, (root,) in enumerate(test_cases):
        p = root.children[0]
        sibling = root.children[1]
        q = Node(4)
        p.children.append(q)
        result = Solution().moveSubTree(root, p, q)
        assert result is root and root.children == [q, sibling]
        assert q.children == [p] and p.children == []
        assert sibling.val == 3
