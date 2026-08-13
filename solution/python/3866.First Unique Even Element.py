from collections import Counter


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        counts = Counter(nums)
        for value in nums:
            if value % 2 == 0 and counts[value] == 1:
                return value
        return -1


if __name__ == "__main__":
    test_cases = [
        ([3, 4, 2, 5, 4, 6], 2),
        ([4, 4], -1),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().firstUniqueEven(nums) == expected
