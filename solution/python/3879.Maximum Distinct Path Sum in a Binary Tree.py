from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSum(self, root: Optional[TreeNode]) -> int:
        def build_graph() -> tuple[list[list[int]], list[int]]:
            adjacency: list[list[int]] = []
            values: list[int] = []
            queue = deque([(root, -1)])
            while queue:
                node, parent = queue.popleft()
                index = len(values)
                values.append(node.val)
                adjacency.append([])
                if parent != -1:
                    adjacency[index].append(parent)
                    adjacency[parent].append(index)
                for child in (node.left, node.right):
                    if child is not None:
                        queue.append((child, index))
            return adjacency, values

        def best_from(start: int) -> int:
            best = float("-inf")
            total = 0
            seen_values: set[int] = set()
            stack = [(1, start, -1)]
            while stack:
                step, node, parent = stack.pop()
                if step == 1:
                    if values[node] in seen_values:
                        continue
                    stack.append((2, node, parent))
                    seen_values.add(values[node])
                    total += values[node]
                    best = max(best, total)
                    for nxt in adjacency[node]:
                        if nxt != parent:
                            stack.append((1, nxt, node))
                else:
                    total -= values[node]
                    seen_values.remove(values[node])
            return best

        adjacency, values = build_graph()
        return max(best_from(node) for node in range(len(values)))


if __name__ == "__main__":
    root1 = TreeNode(2, TreeNode(2), TreeNode(1))
    root2 = TreeNode(1, TreeNode(-2), TreeNode(5, TreeNode(3), TreeNode(5)))
    test_cases = [
        (root1, 3),
        (root2, 9),
    ]
    for _, (root, expected) in enumerate(test_cases):
        assert Solution().maxSum(root) == expected
