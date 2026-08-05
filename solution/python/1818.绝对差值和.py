"""1818. 绝对差值和"""

from bisect import bisect_left


class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        mod = 1_000_000_007
        ordered = sorted(nums1)
        total = 0
        best_reduction = 0
        for first, second in zip(nums1, nums2):
            difference = abs(first - second)
            total += difference
            position = bisect_left(ordered, second)
            if position < len(ordered):
                best_reduction = max(
                    best_reduction, difference - abs(ordered[position] - second)
                )
            if position:
                best_reduction = max(
                    best_reduction, difference - abs(ordered[position - 1] - second)
                )
        return (total - best_reduction) % mod


if __name__ == "__main__":
    test_cases = [
        (([1, 7, 5], [2, 3, 5]), 3),
        (([2, 4, 6, 8, 10], [2, 4, 6, 8, 10]), 0),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minAbsoluteSumDiff(*args) == expected
