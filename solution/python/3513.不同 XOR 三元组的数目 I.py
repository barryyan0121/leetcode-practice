class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        return 1 << n.bit_length()


if __name__ == "__main__":
    test_cases = [
        ([1], 1),
        ([1, 2], 2),
        ([3, 1, 2], 4),
        (list(range(1, 4)), 4),
        (list(range(1, 8)), 8),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().uniqueXorTriplets(nums) == expected
