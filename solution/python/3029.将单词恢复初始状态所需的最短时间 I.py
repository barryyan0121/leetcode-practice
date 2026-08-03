class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length = len(word)
        for time in range(k, length + k, k):
            if word[time:] == word[: length - time]:
                return time // k
        return (length + k - 1) // k


if __name__ == "__main__":
    test_cases = [(("abacaba", 3), 2), (("abacaba", 4), 1), (("abcbabcd", 2), 4)]
    for _, ((word, k), expected) in enumerate(test_cases):
        assert Solution().minimumTimeToInitialState(word, k) == expected
