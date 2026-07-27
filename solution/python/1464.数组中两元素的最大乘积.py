class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        largest = second = 0
        for num in nums:
            if num >= largest:
                largest, second = num, largest
            elif num > second:
                second = num
        return (largest - 1) * (second - 1)


if __name__ == "__main__":
    test_cases = [
        ([3, 4, 5, 2], 12),
        ([1, 5, 4, 5], 16),
        ([3, 7], 12),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maxProduct(nums) == expected
