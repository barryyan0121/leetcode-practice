class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char == ",":
                continue
            if char != ")":
                stack.append(char)
                continue
            values = []
            while stack[-1] != "(":
                values.append(stack.pop())
            stack.pop()
            operator = stack.pop()
            if operator == "!":
                stack.append("t" if values[0] == "f" else "f")
            elif operator == "&":
                stack.append("t" if all(value == "t" for value in values) else "f")
            else:
                stack.append("t" if any(value == "t" for value in values) else "f")
        return stack[-1] == "t"


if __name__ == "__main__":
    test_cases = [
        ("!(f)", True),
        ("|(f,t)", True),
        ("&(t,f)", False),
        ("|(&(t,f,t),!(t))", False),
        ("&(|(f),!(f),t)", False),
    ]
    for _, (expression, expected) in enumerate(test_cases):
        assert Solution().parseBoolExpr(expression) == expected
