class Solution:
    def maxScore(self, nums: list[int]) -> int:
        if len(nums) % 2:
            remaining = min(nums)
        else:
            remaining = min(
                nums[index] + nums[index + 1] for index in range(len(nums) - 1)
            )
        return sum(nums) - remaining


if __name__ == "__main__":
    test_cases = [(([2, 4, 1],), 6), (([5, -1, 4, 2],), 7)]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().maxScore(nums) == expected
