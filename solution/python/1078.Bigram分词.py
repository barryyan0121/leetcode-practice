class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split()
        return [
            words[i + 2]
            for i in range(len(words) - 2)
            if words[i] == first and words[i + 1] == second
        ]


if __name__ == "__main__":
    test_cases = [
        (
            "alice is a good girl she is a good student",
            "a",
            "good",
            ["girl", "student"],
        ),
        ("we will we will rock you", "we", "will", ["we", "rock"]),
        ("hello world", "a", "b", []),
    ]
    for _, (text, first, second, expected) in enumerate(test_cases):
        assert Solution().findOcurrences(text, first, second) == expected
