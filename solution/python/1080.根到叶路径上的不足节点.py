class Solution:
    def sufficientSubset(self, root, limit: int):
        if not root.left and not root.right:
            return root if root.val >= limit else None
        remaining = limit - root.val
        root.left = self.sufficientSubset(root.left, remaining) if root.left else None
        root.right = (
            self.sufficientSubset(root.right, remaining) if root.right else None
        )
        return root if root.left or root.right else None


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), "."))
    from common.node import TreeNode

    test_cases = [
        ([1, 2, -3, -5, None, 4, None], -1, "1,null,-3,4,null,null,null"),
        (
            [5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3],
            22,
            "5,4,11,7,null,null,null,null,8,17,null,null,4,5,null,null,null",
        ),
        ([1, 2, 3], 10, "null"),
    ]
    for _, (values, limit, expected) in enumerate(test_cases):
        result = Solution().sufficientSubset(TreeNode.create_root(values), limit)
        assert TreeNode.print_tree(result) == expected
