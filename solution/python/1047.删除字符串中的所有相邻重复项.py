class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


if __name__ == "__main__":
    test_cases = [("abbaca", "ca"), ("azxxzy", "ay"), ("aaaaaaaa", "")]
    for _, (text, expected) in enumerate(test_cases):
        assert Solution().removeDuplicates(text) == expected
