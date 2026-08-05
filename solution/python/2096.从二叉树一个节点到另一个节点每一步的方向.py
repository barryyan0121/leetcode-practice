"""2096. 从二叉树一个节点到另一个节点每一步的方向"""


class Solution:
    def getDirections(self, root, startValue: int, destValue: int) -> str:
        def path(node, target, result):
            if not node:
                return False
            if node.val == target:
                return True
            result.append("L")
            if path(node.left, target, result):
                return True
            result.pop()
            result.append("R")
            if path(node.right, target, result):
                return True
            result.pop()
            return False

        start, destination = [], []
        path(root, startValue, start)
        path(root, destValue, destination)
        common = 0
        while (
            common < len(start)
            and common < len(destination)
            and start[common] == destination[common]
        ):
            common += 1
        return "U" * (len(start) - common) + "".join(destination[common:])


if __name__ == "__main__":
    test_cases = [(None, "")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().getDirections(None, 1, 1) == expected
