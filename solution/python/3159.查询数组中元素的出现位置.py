class Solution:
    def occurrencesOfElement(
        self, nums: list[int], queries: list[int], x: int
    ) -> list[int]:
        positions = [index for index, value in enumerate(nums) if value == x]
        return [
            positions[query - 1] if query <= len(positions) else -1 for query in queries
        ]


if __name__ == "__main__":
    test_cases = [([1, 3, 1, 7], [1, 2, 3], 1, [0, 2, -1])]
    for _, (nums, queries, x, expected) in enumerate(test_cases):
        assert Solution().occurrencesOfElement(nums, queries, x) == expected
