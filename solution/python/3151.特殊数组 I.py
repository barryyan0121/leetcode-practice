class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        return all((left - right) % 2 for left, right in zip(nums, nums[1:]))


if __name__ == "__main__":
    test_cases = [([1], True), ([2, 1, 4], True), ([4, 3, 1, 6], False)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().isArraySpecial(nums) == expected
