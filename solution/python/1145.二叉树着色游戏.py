class Solution:
    def btreeGameWinningMove(self, root, n: int, x: int) -> bool:
        left_size = right_size = 0

        def count(node):
            nonlocal left_size, right_size
            if not node:
                return 0
            left = count(node.left)
            right = count(node.right)
            if node.val == x:
                left_size, right_size = left, right
            return left + right + 1

        count(root)
        return max(left_size, right_size, n - left_size - right_size - 1) > n // 2


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), "."))
    from common.node import TreeNode

    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11, 3, True),
        ([1, 2, 3], 3, 1, False),
        ([1], 1, 1, False),
    ]
    for _, (values, n, x, expected) in enumerate(test_cases):
        assert (
            Solution().btreeGameWinningMove(TreeNode.create_root(values), n, x)
            == expected
        )
