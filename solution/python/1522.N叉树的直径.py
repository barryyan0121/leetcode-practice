class Node:
    def __init__(self, val: int = 0, children=None):
        self.val = val
        self.children = children or []


class Solution:
    def diameter(self, root: Node) -> int:
        if not root:
            return 0
        heights = {}
        stack = [(root, False)]
        answer = 0
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                stack.extend((child, False) for child in node.children)
                continue
            first = second = 0
            for child in node.children:
                height = heights[child] + 1
                if height > first:
                    first, second = height, first
                elif height > second:
                    second = height
            heights[node] = first
            answer = max(answer, first + second)
        return answer


if __name__ == "__main__":
    test_cases = [(Node(1, [Node(2), Node(3)]), 2)]
    for _, (root, expected) in enumerate(test_cases):
        root.children[0].children.append(Node(4))
        assert Solution().diameter(root) == expected + 1
