"""1973. 值等于子节点值之和的节点数量"""

from typing import Optional

from common.node import TreeNode


class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal answer
            if node is None:
                return 0
            children_sum = dfs(node.left) + dfs(node.right)
            answer += node.val == children_sum
            return node.val + children_sum

        dfs(root)
        return answer


if __name__ == "__main__":
    test_cases = [((None,), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().equalToDescendants(*args) == expected
