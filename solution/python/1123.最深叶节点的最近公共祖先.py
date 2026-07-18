class Solution:
    def lcaDeepestLeaves(self, root):
        def dfs(node):
            if not node:
                return None, 0
            left, left_depth = dfs(node.left)
            right, right_depth = dfs(node.right)
            if left_depth == right_depth:
                return node, left_depth + 1
            return (
                (left, left_depth + 1)
                if left_depth > right_depth
                else (right, right_depth + 1)
            )

        return dfs(root)[0]


if __name__ == "__main__":
    import os, sys

    sys.path.append(os.path.join(os.path.dirname(__file__), "."))
    from common.node import TreeNode

    test_cases = [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 2),
        ([1], 1),
        ([0, 1, 3, None, 2], 2),
    ]
    for _, (values, expected) in enumerate(test_cases):
        assert Solution().lcaDeepestLeaves(TreeNode.create_root(values)).val == expected
