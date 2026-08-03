class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        for index in range(len(nums) - 2):
            if nums[index] == 0:
                operations += 1
                nums[index + 1] ^= 1
                nums[index + 2] ^= 1
        return operations if nums[-1] == nums[-2] == 1 else -1


if __name__ == "__main__":
    test_cases = [([0, 1, 1, 1, 0, 0], 3), ([0, 1, 1, 1], -1)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().minOperations(nums) == expected
