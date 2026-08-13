"""2458. 移除子树后的二叉树高度"""


class Solution:
    def treeQueries(self, root, queries: list[int]) -> list[int]:
        order = []
        depths = {}
        starts = {}
        ends = {}

        def dfs(node, depth):
            if node is None:
                return
            start = len(order)
            order.append(node.val)
            starts[node.val] = start
            depths[node.val] = depth
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            ends[node.val] = len(order)

        dfs(root, 0)
        prefix = []
        current = -1
        for value in order:
            current = max(current, depths[value])
            prefix.append(current)
        suffix = [-1] * len(order)
        current = -1
        for index in range(len(order) - 1, -1, -1):
            current = max(current, depths[order[index]])
            suffix[index] = current
        answer = []
        for query in queries:
            left = starts[query]
            right = ends[query]
            outside = max(
                prefix[left - 1] if left else -1,
                suffix[right] if right < len(order) else -1,
            )
            answer.append(outside)
        return answer

if __name__ == "__main__":
    class Node:
        def __init__(self, val, left=None, right=None): self.val, self.left, self.right = val, left, right
    root = Node(1, Node(2, Node(4), Node(5)), Node(3))
    assert Solution().treeQueries(root, [2,3]) == [1,2]
