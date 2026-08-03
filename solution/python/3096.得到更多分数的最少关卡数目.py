class Solution:
    def minimumLevels(self, possible: list[int]) -> int:
        scores = [1 if value else -1 for value in possible]
        total = sum(scores)
        prefix = 0
        for index, score in enumerate(scores[:-1], 1):
            prefix += score
            if prefix > total - prefix:
                return index
        return -1


if __name__ == "__main__":
    test_cases = [([1, 0, 1, 0], 1), ([1, 1, 1, 1, 1], 3), ([0, 0], -1)]
    for _, (possible, expected) in enumerate(test_cases):
        assert Solution().minimumLevels(possible) == expected
