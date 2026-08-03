class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        total = 0
        for number in nums:
            digits = str(number)
            total += int(max(digits) * len(digits))
        return total


if __name__ == "__main__":
    test_cases = [([10, 21, 31], 66), ([2, 2, 2], 6)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().sumOfEncryptedInt(nums) == expected
