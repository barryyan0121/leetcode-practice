"""3572. 选择不同 X 值三元组使 Y 值之和最大"""


class Solution:
    def maxSumDistinctTriplet(self, x: list[int], y: list[int]) -> int:
        best = {}
        for value, score in zip(x, y):
            best[value] = max(best.get(value, 0), score)
        return sum(sorted(best.values(), reverse=True)[:3]) if len(best) >= 3 else -1


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 1, 3, 2], [5, 3, 4, 6, 2]), 14),
        (([1, 2, 1, 2], [4, 5, 6, 7]), -1),
    ]
    for _, ((x, y), expected) in enumerate(test_cases):
        assert Solution().maxSumDistinctTriplet(x, y) == expected
