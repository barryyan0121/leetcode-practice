from bisect import bisect_left, bisect_right
from collections import Counter


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        ordered = sorted(nums)
        frequencies = Counter(nums)
        answer = 0
        candidates = set()
        for value in nums:
            candidates.update((value - k, value, value + k))
        for target in candidates:
            left = bisect_left(ordered, target - k)
            right = bisect_right(ordered, target + k)
            in_range = right - left
            answer = max(answer, min(in_range, frequencies[target] + numOperations))
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 4, 5], 1, 2), 2),
        (([5, 11, 20, 20], 5, 1), 2),
        (([1, 2, 3], 0, 2), 1),
    ]
    for _, ((nums, k, operations), expected) in enumerate(test_cases):
        assert Solution().maxFrequency(nums, k, operations) == expected
