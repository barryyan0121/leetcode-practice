class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        return sum(a != b for a, b in zip(heights, sorted(heights)))


if __name__ == "__main__":
    test_cases = [([1, 1, 4, 2, 1, 3], 3)]
    for _, (heights, expected) in enumerate(test_cases):
        assert Solution().heightChecker(heights) == expected
