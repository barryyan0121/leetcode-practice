from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        return max(
            (num for num, count in Counter(nums).items() if count == 1), default=-1
        )


if __name__ == "__main__":
    test_cases = [
        ([5, 7, 3, 9, 4, 9, 8, 3, 1], 8),
        ([9, 9, 8, 8], -1),
        ([1], 1),
        ([1, 1, 2, 2, 3], 3),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().largestUniqueNumber(nums) == expected
