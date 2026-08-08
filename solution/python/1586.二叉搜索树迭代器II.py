class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.values = []
        self.index = -1
        self.stack = []
        self._push_left(root)

    def next(self) -> int:
        self.index += 1
        if self.index == len(self.values):
            node = self.stack.pop()
            self.values.append(node.val)
            self._push_left(node.right)
        return self.values[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.values) or bool(self.stack)

    def prev(self) -> int:
        self.index -= 1
        return self.values[self.index]

    def hasPrev(self) -> bool:
        return self.index > 0

    def _push_left(self, node: TreeNode) -> None:
        while node:
            self.stack.append(node)
            node = node.left


if __name__ == "__main__":
    test_cases = [(TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20))),)]
    for _, (root,) in enumerate(test_cases):
        iterator = BSTIterator(root)
        assert iterator.next() == 3 and iterator.next() == 7
        assert iterator.hasPrev() and iterator.prev() == 3
        assert iterator.next() == 7 and iterator.next() == 9
