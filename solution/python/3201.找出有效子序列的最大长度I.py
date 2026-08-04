class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        same = max(sum(number % 2 == parity for number in nums) for parity in (0, 1))
        alternating = 0
        for expected in (0, 1):
            length = 0
            for number in nums:
                if number % 2 == expected:
                    length += 1
                    expected ^= 1
            alternating = max(alternating, length)
        return max(same, alternating)


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4], 4), ([1, 2, 1, 1, 2, 1, 2], 6), ([1, 3], 2)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maximumLength(nums) == expected
