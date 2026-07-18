class Solution:
    def sumOfDigits(self, nums: list[int]) -> int:
        return 1 if sum(map(int, str(min(nums)))) % 2 == 0 else 0


if __name__ == "__main__":
    test_cases = [
        ([34, 23, 1, 24, 75, 33, 54, 8], 0),
        ([99, 77, 33, 66, 55], 1),
        ([10], 0),
        ([100], 0),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().sumOfDigits(nums) == expected
