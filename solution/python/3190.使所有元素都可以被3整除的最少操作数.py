class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return sum(min(number % 3, 3 - number % 3) for number in nums)


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4], 3), ([3, 6, 9], 0)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().minimumOperations(nums) == expected
