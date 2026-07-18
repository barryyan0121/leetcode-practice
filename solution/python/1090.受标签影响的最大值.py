from collections import defaultdict


class Solution:
    def largestValsFromLabels(
        self, values: list[int], labels: list[int], num_wanted: int, use_limit: int
    ) -> int:
        used = defaultdict(int)
        total = 0
        for value, label in sorted(zip(values, labels), reverse=True):
            if used[label] < use_limit:
                total += value
                used[label] += 1
                num_wanted -= 1
                if not num_wanted:
                    return total
        return total


if __name__ == "__main__":
    test_cases = [
        ([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1, 9),
        ([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 2, 12),
        ([9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 1, 16),
        ([1, 2], [1, 1], 2, 1, 2),
    ]
    for _, (values, labels, num_wanted, use_limit, expected) in enumerate(test_cases):
        assert (
            Solution().largestValsFromLabels(values, labels, num_wanted, use_limit)
            == expected
        )
