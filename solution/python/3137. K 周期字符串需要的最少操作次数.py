from collections import Counter


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        blocks = [word[index : index + k] for index in range(0, len(word), k)]
        return len(blocks) - Counter(blocks).most_common(1)[0][1]


if __name__ == "__main__":
    test_cases = [("leetcodeleet", 4, 1), ("leetcoleet", 2, 3)]
    for _, (word, k, expected) in enumerate(test_cases):
        assert Solution().minimumOperationsToMakeKPeriodic(word, k) == expected
