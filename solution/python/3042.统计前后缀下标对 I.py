class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        answer = 0
        for right, word in enumerate(words):
            for previous in words[:right]:
                if word.startswith(previous) and word.endswith(previous):
                    answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [(["a", "aba", "ababa", "aa"], 4), (["pa", "papa", "ma", "mama"], 2)]
    for _, (words, expected) in enumerate(test_cases):
        assert Solution().countPrefixSuffixPairs(words) == expected
