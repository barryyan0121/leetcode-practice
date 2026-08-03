class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = sorted(
            (word.count(character) for character in set(word)), reverse=True
        )
        return sum(
            frequency * (index // 8 + 1) for index, frequency in enumerate(frequencies)
        )


if __name__ == "__main__":
    test_cases = [("abcde", 5), ("aabbccddeeffgghhiiii", 22)]
    for _, (word, expected) in enumerate(test_cases):
        assert Solution().minimumPushes(word) == expected
