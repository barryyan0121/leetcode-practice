from random import randrange


class Solution:
    def getResults(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        class Node:
            __slots__ = "value", "priority", "left", "right", "size", "xor", "reverse"

            def __init__(self, value: int):
                self.value = self.xor = value
                self.priority = randrange(1 << 30)
                self.left = self.right = None
                self.size = 1
                self.reverse = False

        def size(node: Node | None) -> int:
            return node.size if node else 0

        def value_xor(node: Node | None) -> int:
            return node.xor if node else 0

        def update(node: Node) -> None:
            node.size = 1 + size(node.left) + size(node.right)
            node.xor = value_xor(node.left) ^ node.value ^ value_xor(node.right)

        def push(node: Node | None) -> None:
            if node and node.reverse:
                node.left, node.right = node.right, node.left
                for child in (node.left, node.right):
                    if child:
                        child.reverse = not child.reverse
                node.reverse = False

        def merge(left: Node | None, right: Node | None) -> Node | None:
            if not left or not right:
                return left or right
            if left.priority > right.priority:
                push(left)
                left.right = merge(left.right, right)
                update(left)
                return left
            push(right)
            right.left = merge(left, right.left)
            update(right)
            return right

        def split(node: Node | None, count: int) -> tuple[Node | None, Node | None]:
            if not node:
                return None, None
            push(node)
            if size(node.left) >= count:
                left, node.left = split(node.left, count)
                update(node)
                return left, node
            node.right, right = split(node.right, count - size(node.left) - 1)
            update(node)
            return node, right

        root = None
        for value in nums:
            root = merge(root, Node(value))

        answer = []
        for query in queries:
            kind, left, right = query
            if kind == 1:
                first, rest = split(root, left)
                middle, last = split(rest, 1)
                middle.value = right
                update(middle)
                root = merge(first, merge(middle, last))
                continue
            first, rest = split(root, left)
            middle, last = split(rest, right - left + 1)
            if kind == 2:
                answer.append(value_xor(middle))
            else:
                if middle:
                    middle.reverse = not middle.reverse
            root = merge(first, merge(middle, last))
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5], [[2, 1, 3], [1, 2, 10], [3, 0, 4], [2, 0, 4]]), [5, 8]),
        (([7, 8, 9], [[1, 0, 3], [2, 0, 2], [3, 1, 2]]), [2]),
    ]
    for _, ((nums, queries), expected) in enumerate(test_cases):
        assert Solution().getResults(nums, queries) == expected
