class Solution:
    def kthLargestPerfectSubtree(self, root, k: int) -> int:
        sizes = []

        def visit(node) -> int:
            if node is None:
                return 0
            left, right = visit(node.left), visit(node.right)
            if left != right or left < 0:
                return -1
            size = left * 2 + 1
            sizes.append(size)
            return size

        visit(root)
        sizes.sort(reverse=True)
        return sizes[k - 1] if k <= len(sizes) else -1


if __name__ == "__main__":

    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val, self.left, self.right = value, left, right

    def create_tree(values):
        nodes = [None if value is None else TreeNode(value) for value in values]
        children = iter(nodes[1:])
        for node in nodes:
            if node is not None:
                node.left = next(children, None)
                node.right = next(children, None)
        return nodes[0]

    test_cases = [
        ((create_tree([1, 2, 3, 4, 5, 6, 7]), 1), 7),
        ((create_tree([1, 2, 3, 4, None, None, 5]), 2), 1),
    ]
    for _, ((root, k), expected) in enumerate(test_cases):
        assert Solution().kthLargestPerfectSubtree(root, k) == expected
