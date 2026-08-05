class Solution:
    def canSplitArray(self, nums: list[int], m: int) -> bool:
        return len(nums) <= 2 or any(a + b >= m for a, b in zip(nums, nums[1:]))


if __name__ == "__main__":
    assert Solution().canSplitArray([2, 2, 1], 4) is True
