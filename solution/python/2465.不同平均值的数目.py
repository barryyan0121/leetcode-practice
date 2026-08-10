"""2465. 不同平均值的数目"""


class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        return len({nums[left] + nums[~left] for left in range(len(nums) // 2)})
