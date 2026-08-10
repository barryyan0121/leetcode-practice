class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: list["TreeNode"]
    ) -> "TreeNode":
        targets = set(nodes)

        def find(node):
            if node is None or node in targets:
                return node
            left, right = find(node.left), find(node.right)
            if left is not None and right is not None:
                return node
            return left or right

        return find(root)


if __name__ == "__main__":

    class TreeNode:
        def __init__(self, val, left=None, right=None):
            self.val, self.left, self.right = val, left, right

    root = TreeNode(3, TreeNode(5), TreeNode(1))
    root.left.left, root.left.right = TreeNode(6), TreeNode(2)
    root.left.right.left, root.left.right.right = TreeNode(7), TreeNode(4)
    test_cases = [([root.left.right.left, root.left.right.right], 2), ([root.left], 5)]
    for index, (nodes, expected) in enumerate(test_cases):
        assert Solution().lowestCommonAncestor(root, nodes).val == expected, index
