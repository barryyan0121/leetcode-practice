class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        draxemilon = nums
        even = sum(value % 2 == 0 for value in nums)
        return [0] * even + [1] * (len(nums) - even)


if __name__ == "__main__":
    test_cases = [
        (([4, 3, 2, 1],), [0, 0, 1, 1]),
        (([1, 5, 1, 4, 2],), [0, 0, 1, 1, 1]),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().transformArray(nums) == expected
