class Solution:
    def delNodes(self, root, to_delete: list[int]):
        removed = set(to_delete)
        forest = []

        def dfs(node, is_root: bool):
            if not node:
                return None
            deleted = node.val in removed
            if is_root and not deleted:
                forest.append(node)
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)
            return None if deleted else node

        dfs(root, True)
        return forest


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), "."))
    from common.node import TreeNode

    test_cases = [
        (
            [1, 2, 3, 4, 5, 6, 7],
            [3, 5],
            ["1,2,4,null,null,null,null", "6,null,null", "7,null,null"],
        ),
        ([1, 2, 3], [1], ["2,null,null", "3,null,null"]),
        ([1], [1], []),
    ]
    for _, (values, to_delete, expected) in enumerate(test_cases):
        forest = Solution().delNodes(TreeNode.create_root(values), to_delete)
        assert [TreeNode.print_tree(root) for root in forest] == expected
