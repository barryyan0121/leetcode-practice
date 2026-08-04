class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        draxemilon = (nums, k)
        size = len(nums)
        return sum(
            value
            for index, value in enumerate(nums)
            if (index < k or value > nums[index - k])
            and (index + k >= size or value > nums[index + k])
        )


if __name__ == "__main__":
    test_cases = [
        (([1, 3, 2, 1, 5, 4], 2), 12),
        (([2, 1], 1), 2),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().sumOfGoodNumbers(nums, k) == expected
