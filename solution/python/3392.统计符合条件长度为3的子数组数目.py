class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        return sum(
            2 * (nums[index] + nums[index + 2]) == nums[index + 1]
            for index in range(len(nums) - 2)
        )


if __name__ == "__main__":
    assert Solution().countSubarrays([1, 2, 1, 4, 1]) == 1
    assert Solution().countSubarrays([1, 1, 1]) == 0
