from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lengths = {}
        for value in arr:
            lengths[value] = lengths.get(value - difference, 0) + 1
        return max(lengths.values())


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], 1, 4),
        ([1, 3, 5, 7], 1, 1),
        ([1, 5, 7, 8, 5, 3, 4, 2, 1], -2, 4),
    ]
    for _, (arr, difference, expected) in enumerate(test_cases):
        assert Solution().longestSubsequence(arr, difference) == expected
