class Solution:
    def minOperations(self, nums: list[int]) -> int:
        flipped = 0
        operations = 0
        for number in nums:
            if number ^ flipped == 0:
                operations += 1
                flipped ^= 1
        return operations


if __name__ == "__main__":
    test_cases = [([0, 1, 1, 0, 1], 4), ([1, 0, 0, 0], 1)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().minOperations(nums) == expected
