"""2567. 修改两个元素后的最小分数"""


class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])


if __name__ == "__main__":
    assert Solution().minimizeSum([1, 4, 7, 8, 5]) == 3
