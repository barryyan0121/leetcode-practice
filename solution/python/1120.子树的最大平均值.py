class Solution:
    def maximumAverageSubtree(self, root) -> float:
        best = float("-inf")

        def dfs(node):
            nonlocal best
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total = node.val + left_sum + right_sum
            count = left_count + right_count + 1
            best = max(best, total / count)
            return total, count

        dfs(root)
        return best


if __name__ == "__main__":
    import os, sys

    sys.path.append(os.path.join(os.path.dirname(__file__), "."))
    from common.node import TreeNode

    test_cases = [([5, 6, 1], 6.0), ([0, None, 1], 1.0), ([-5, -1, -3], -1.0)]
    for _, (values, expected) in enumerate(test_cases):
        assert (
            abs(
                Solution().maximumAverageSubtree(TreeNode.create_root(values))
                - expected
            )
            < 1e-9
        )
