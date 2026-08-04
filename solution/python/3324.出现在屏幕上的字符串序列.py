class Solution:
    def stringSequence(self, target: str) -> list[str]:
        current = []
        answer = []
        for character in target:
            current.append("a")
            answer.append("".join(current))
            while current[-1] != character:
                current[-1] = chr(ord(current[-1]) + 1)
                answer.append("".join(current))
        return answer


if __name__ == "__main__":
    test_cases = [
        (("abc",), ["a", "aa", "ab", "aba", "abb", "abc"]),
        (
            ("he",),
            ["a", "b", "c", "d", "e", "f", "g", "h", "ha", "hb", "hc", "hd", "he"],
        ),
    ]
    for _, ((target,), expected) in enumerate(test_cases):
        assert Solution().stringSequence(target) == expected
