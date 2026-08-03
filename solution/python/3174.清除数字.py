class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for character in s:
            if character.isdigit():
                stack.pop()
            else:
                stack.append(character)
        return "".join(stack)


if __name__ == "__main__":
    test_cases = [("abc", "abc"), ("cb34", ""), ("a1b2c3", "")]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().clearDigits(s) == expected
