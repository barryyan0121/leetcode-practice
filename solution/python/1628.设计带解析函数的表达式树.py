from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class ValueNode(Node):
    def __init__(self, value: int):
        self.value = value

    def evaluate(self) -> int:
        return self.value


class OperatorNode(Node):
    def __init__(self, operator: str, left: Node, right: Node):
        self.operator = operator
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        left, right = self.left.evaluate(), self.right.evaluate()
        if self.operator == "+":
            return left + right
        if self.operator == "-":
            return left - right
        if self.operator == "*":
            return left * right
        return (1 if left * right >= 0 else -1) * (abs(left) // abs(right))


class TreeBuilder:
    def buildTree(self, postfix: list[str]) -> Node:
        stack: list[Node] = []
        operators = {"+", "-", "*", "/"}
        for token in postfix:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(OperatorNode(token, left, right))
            else:
                stack.append(ValueNode(int(token)))
        return stack[-1]


if __name__ == "__main__":
    test_cases = [
        (["3", "4", "+", "2", "*", "7", "/"], 2),
        (["4", "5", "7", "2", "+", "-", "*"], -16),
    ]
    for index, (postfix, expected) in enumerate(test_cases):
        assert TreeBuilder().buildTree(postfix).evaluate() == expected, index
