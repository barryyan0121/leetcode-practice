from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        counts = Counter()
        answer = 0
        for first, second in dominoes:
            key = min(first, second) * 10 + max(first, second)
            answer += counts[key]
            counts[key] += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        ([[1, 2], [2, 1], [3, 4], [5, 6]], 1),
        ([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]], 3),
        ([[1, 1], [1, 1]], 1),
    ]
    for _, (dominoes, expected) in enumerate(test_cases):
        assert Solution().numEquivDominoPairs(dominoes) == expected
