from common.node import TreeNode


class FindElements:
    def __init__(self, root: TreeNode):
        self.values = set()
        stack = [(root, 0)]
        while stack:
            node, value = stack.pop()
            self.values.add(value)
            if node.left:
                stack.append((node.left, value * 2 + 1))
            if node.right:
                stack.append((node.right, value * 2 + 2))

    def find(self, target: int) -> bool:
        return target in self.values


if __name__ == "__main__":
    test_cases = [
        (TreeNode.create_root([-1, -1, -1]), [0, 1, 2, 3], [True, True, True, False])
    ]
    for _, (root, targets, expected) in enumerate(test_cases):
        finder = FindElements(root)
        assert [finder.find(target) for target in targets] == expected
