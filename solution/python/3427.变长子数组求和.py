class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        return sum(
            prefix[index + 1] - prefix[max(0, index - value)]
            for index, value in enumerate(nums)
        )


if __name__ == "__main__":
    test_cases = [
        (([2, 3, 1],), 11),
        (([3, 1, 1, 2],), 13),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().subarraySum(nums) == expected
