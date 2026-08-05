"""1932. 合并多棵二叉搜索树"""


class Solution:
    def canMerge(self, trees: list) -> object:
        roots = {tree.val: tree for tree in trees}
        leaf_values = set()
        for tree in trees:
            if tree.left:
                leaf_values.add(tree.left.val)
            if tree.right:
                leaf_values.add(tree.right.val)
        candidates = [tree for tree in trees if tree.val not in leaf_values]
        if len(candidates) != 1:
            return None
        root = candidates[0]
        used = {root.val}

        def merge(node: object, low: int, high: int) -> bool:
            if node.val <= low or node.val >= high:
                return False
            if (
                node.left is None
                and node.right is None
                and node.val in roots
                and node.val not in used
            ):
                replacement = roots[node.val]
                node.left = replacement.left
                node.right = replacement.right
                used.add(node.val)
            return (node.left is None or merge(node.left, low, node.val)) and (
                node.right is None or merge(node.right, node.val, high)
            )

        if not merge(root, -(10**9), 10**9) or len(used) != len(trees):
            return None
        return root


if __name__ == "__main__":

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val, self.left, self.right = val, left, right

    test_cases = [
        (
            (
                [
                    TreeNode(2, TreeNode(1)),
                    TreeNode(3, TreeNode(2), TreeNode(5)),
                    TreeNode(5, TreeNode(4)),
                ],
            ),
            3,
        ),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().canMerge(*args).val == expected
