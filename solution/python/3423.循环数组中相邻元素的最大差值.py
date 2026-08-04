class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        return max(abs(left - right) for left, right in zip(nums, nums[1:] + nums[:1]))


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 4],), 3),
        (([-5, -10, -5],), 5),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().maxAdjacentDistance(nums) == expected
