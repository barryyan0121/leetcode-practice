from collections import Counter


class Solution:
    def canDivideIntoSubsequences(self, nums: list[int], k: int) -> bool:
        return max(Counter(nums).values()) * k <= len(nums)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 3, 3, 4, 4], 3, True),
        ([5, 6, 6, 7, 8], 3, False),
        ([1, 1, 2, 2, 3, 3], 3, True),
    ]
    for _, (nums, k, expected) in enumerate(test_cases):
        assert Solution().canDivideIntoSubsequences(nums, k) == expected
