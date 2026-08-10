class Solution:
    def flipBinaryTree(self, root: "Node", leaf: "Node") -> "Node":
        path = [leaf]
        while path[-1].parent is not None:
            path.append(path[-1].parent)
        for index in range(len(path) - 1):
            current, parent = path[index], path[index + 1]
            if parent.left is current:
                parent.left = None
            else:
                parent.right = None
            if current.left is not None:
                current.right = current.left
                current.left.parent = current
                current.left = None
            current.left = parent
            parent.parent = current
            current.parent = path[index - 1] if index else None
        return leaf


if __name__ == "__main__":

    class Node:
        def __init__(self, val):
            self.val = val
            self.left = self.right = self.parent = None

    test_cases = []
    root = Node(3)
    five, two, seven = Node(5), Node(2), Node(7)
    root.left, five.parent = five, root
    five.right, two.parent = two, five
    two.left, seven.parent = seven, two
    test_cases.append((root, seven, [7, 2, 5, 3]))
    for index, (tree, leaf, expected) in enumerate(test_cases):
        result = Solution().flipBinaryTree(tree, leaf)
        values = []
        while result:
            values.append(result.val)
            result = result.left
        assert values == expected, index
