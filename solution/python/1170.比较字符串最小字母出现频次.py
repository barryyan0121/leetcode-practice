from bisect import bisect_right


class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        frequency = lambda word: word.count(min(word))
        word_counts = sorted(map(frequency, words))
        return [
            len(words) - bisect_right(word_counts, frequency(query))
            for query in queries
        ]


if __name__ == "__main__":
    test_cases = [(["cbd"], ["zaaaz"], [1])]
    for _, (queries, words, expected) in enumerate(test_cases):
        assert Solution().numSmallerByFrequency(queries, words) == expected
