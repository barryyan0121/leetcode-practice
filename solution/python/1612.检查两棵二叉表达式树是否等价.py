from collections import Counter


class Node:
    def __init__(self, val: str = "", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEquivalence(self, root1: "Node", root2: "Node") -> bool:
        def leaves(root: Node) -> Counter:
            count = Counter()
            stack = [root]
            while stack:
                node = stack.pop()
                if node.val == "+":
                    stack.extend((node.left, node.right))
                else:
                    count[node.val] += 1
            return count

        return leaves(root1) == leaves(root2)


if __name__ == "__main__":
    test_cases = [
        (Node("+", Node("a"), Node("b")), Node("+", Node("b"), Node("a")), True)
    ]
    for _, (first, second, expected) in enumerate(test_cases):
        assert Solution().checkEquivalence(first, second) == expected
