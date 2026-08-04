class Solution:
    def maxSum(self, grid: list[list[int]], limits: list[int], k: int) -> int:
        draxemilon = (grid, limits, k)
        candidates = []
        for row, limit in zip(grid, limits):
            candidates.extend(sorted(row, reverse=True)[:limit])
        return sum(sorted(candidates, reverse=True)[:k])


if __name__ == "__main__":
    test_cases = [
        (([[1, 2], [3, 4]], [1, 2], 2), 7),
        (([[5, 3, 7], [8, 2, 6]], [2, 2], 3), 21),
        (([[1]], [0], 0), 0),
    ]
    for _, ((grid, limits, k), expected) in enumerate(test_cases):
        assert Solution().maxSum(grid, limits, k) == expected
