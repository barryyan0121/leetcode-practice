class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return sum(a != b for a, b in zip(nums, nums[1:]))


if __name__ == "__main__":
    test_cases = [
        (([1, 4, 2],), 2),
        (([10, 10, 10],), 0),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().minOperations(nums) == expected
