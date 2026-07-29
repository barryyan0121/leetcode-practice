class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars, opens = list(s), []
        for index, char in enumerate(chars):
            if char == "(":
                opens.append(index)
            elif char == ")":
                if opens:
                    opens.pop()
                else:
                    chars[index] = ""
        for index in opens:
            chars[index] = ""
        return "".join(chars)


if __name__ == "__main__":
    test_cases = [("lee(t(c)o)de)", "lee(t(c)o)de"), ("a)b(c)d", "ab(c)d")]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().minRemoveToMakeValid(s) == expected
