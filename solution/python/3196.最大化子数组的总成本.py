class Solution:
    def maximumTotalCost(self, nums: list[int]) -> int:
        positive = nums[0]
        negative = -(10**18)
        for number in nums[1:]:
            positive, negative = max(positive, negative) + number, positive - number
        return max(positive, negative)


if __name__ == "__main__":
    test_cases = [([1, -2, 3, 4], 10), ([1, -1, 1, -1], 4), ([0], 0), ([1, -1], 2)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maximumTotalCost(nums) == expected
