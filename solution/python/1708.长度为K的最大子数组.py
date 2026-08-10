class Solution:
    def largestSubarray(self, nums: list[int], k: int) -> list[int]:
        start = max(range(len(nums) - k + 1), key=nums.__getitem__)
        return nums[start : start + k]


if __name__ == "__main__":
    test_cases = [
        (([1, 4, 5, 2, 3], 3), [5, 2, 3]),
        (([1, 4, 5, 2, 3], 4), [4, 5, 2, 3]),
        (([1, 4, 5, 2, 3], 1), [5]),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().largestSubarray(*args) == expected, index
