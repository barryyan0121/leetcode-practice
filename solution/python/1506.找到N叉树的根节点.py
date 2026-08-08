class Node:
    def __init__(self, val: int, children=None):
        self.val = val
        self.children = children or []


class Solution:
    def findRoot(self, tree: list[Node]) -> Node:
        root_value = 0
        nodes = {}
        for node in tree:
            root_value ^= node.val
            nodes[node.val] = node
            for child in node.children:
                root_value ^= child.val
        return nodes[root_value]


if __name__ == "__main__":
    test_cases = [(Node(1, [Node(2), Node(3)]),)]
    for _, (root,) in enumerate(test_cases):
        root.children[0].children.append(Node(4))
        tree = [root.children[1], root.children[0].children[0], root, root.children[0]]
        assert Solution().findRoot(tree) is root
