class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        return sum(
            max(value - index, 0)
            for index, value in enumerate(sorted(happiness, reverse=True)[:k])
        )


if __name__ == "__main__":
    test_cases = [(([1, 2, 3], 2), 4), (([1, 1, 1, 1], 2), 1)]
    for _, ((happiness, k), expected) in enumerate(test_cases):
        assert Solution().maximumHappinessSum(happiness, k) == expected
