from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return sum(count * (count - 1) // 2 for count in Counter(nums).values())


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 1, 1, 3], 4), ([1, 1, 1, 1], 6)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().numIdenticalPairs(nums) == expected
