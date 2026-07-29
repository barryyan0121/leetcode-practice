class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ")":
                part = []
                while stack[-1] != "(":
                    part.append(stack.pop())
                stack.pop()
                stack.extend(part)
            else:
                stack.append(char)
        return "".join(stack)


if __name__ == "__main__":
    test_cases = [("(abcd)", "dcba"), ("(u(love)i)", "iloveu")]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().reverseParentheses(s) == expected
