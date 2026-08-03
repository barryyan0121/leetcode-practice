class Solution:
    def minOperationsToMakeMedianK(self, nums: list[int], k: int) -> int:
        nums.sort()
        middle = len(nums) // 2
        operations = sum(max(0, value - k) for value in nums[: middle + 1])
        operations += sum(max(0, k - value) for value in nums[middle:])
        return operations


if __name__ == "__main__":
    test_cases = [([2, 5, 6, 8, 5], 4, 2), ([2, 5, 6, 8, 5], 7, 3)]
    for _, (nums, k, expected) in enumerate(test_cases):
        assert Solution().minOperationsToMakeMedianK(nums, k) == expected
