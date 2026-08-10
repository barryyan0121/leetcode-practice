class Solution:
    def correctBinaryTree(self, root: "TreeNode") -> "TreeNode":
        visited = set()

        def visit(node):
            if node is None or node.right in visited:
                return None if node is not None else None
            visited.add(node)
            node.right = visit(node.right)
            node.left = visit(node.left)
            return node

        return visit(root)


if __name__ == "__main__":

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val, self.left, self.right = val, left, right

    test_cases = []
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    root.left.right = root.right
    test_cases.append((root, [1, None, 3]))
    for index, (tree, expected) in enumerate(test_cases):
        result = Solution().correctBinaryTree(tree)
        assert [result.val, result.left, result.right.val] == expected, index
