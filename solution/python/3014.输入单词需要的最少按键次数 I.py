class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(index // 8 + 1 for index in range(len(word)))


if __name__ == "__main__":
    test_cases = [("abcde", 5), ("xycdefghij", 12)]
    for _, (word, expected) in enumerate(test_cases):
        assert Solution().minimumPushes(word) == expected
