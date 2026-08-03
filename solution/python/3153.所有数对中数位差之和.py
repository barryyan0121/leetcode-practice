class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        digits = max(len(str(value)) for value in nums)
        answer = 0
        divisor = 1
        for _ in range(digits):
            counts = [0] * 10
            for value in nums:
                counts[(value // divisor) % 10] += 1
            pairs = len(nums) * (len(nums) - 1) // 2
            answer += pairs - sum(count * (count - 1) // 2 for count in counts)
            divisor *= 10
        return answer


if __name__ == "__main__":
    test_cases = [([13, 23, 12], 4), ([10, 10], 0)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().sumDigitDifferences(nums) == expected
