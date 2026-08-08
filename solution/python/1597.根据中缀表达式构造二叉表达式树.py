class Node:
    def __init__(self, val: str = "", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expTree(self, s: str) -> "Node":
        nodes, operators = [], []
        priority = {"+": 1, "-": 1, "*": 2, "/": 2}

        def combine() -> None:
            right, left = nodes.pop(), nodes.pop()
            nodes.append(Node(operators.pop(), left, right))

        for char in s:
            if char.isdigit():
                nodes.append(Node(char))
            elif char == "(":
                operators.append(char)
            elif char == ")":
                while operators[-1] != "(":
                    combine()
                operators.pop()
            else:
                while (
                    operators
                    and operators[-1] != "("
                    and priority[operators[-1]] >= priority[char]
                ):
                    combine()
                operators.append(char)
        while operators:
            combine()
        return nodes[-1]


if __name__ == "__main__":
    test_cases = [("3*4-2*5", 2), ("2-3/(5*2)+1", 2.7)]
    for _, (expression, expected) in enumerate(test_cases):

        def evaluate(node):
            if node.val.isdigit():
                return int(node.val)
            return eval(f"{evaluate(node.left)} {node.val} {evaluate(node.right)}")

        assert abs(evaluate(Solution().expTree(expression)) - expected) < 1e-9
