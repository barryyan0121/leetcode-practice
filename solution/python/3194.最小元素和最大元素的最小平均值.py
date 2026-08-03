class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        nums.sort()
        return min(
            (nums[index] + nums[-index - 1]) / 2 for index in range(len(nums) // 2)
        )


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4], 2.5), ([1, 10, 3, 7], 5.0)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().minimumAverage(nums) == expected
