from collections import Counter


class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        return max(Counter(nums).values()) <= 2


if __name__ == "__main__":
    test_cases = [([1, 1, 2, 2, 3, 4], True), ([1, 1, 1, 1], False)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().isPossibleToSplit(nums) == expected
