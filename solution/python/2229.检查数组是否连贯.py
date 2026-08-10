"""2229. 检查数组是否连贯"""


class Solution:
    def isConsecutive(self, nums: list[int]) -> bool:
        return len(set(nums)) == len(nums) and max(nums) - min(nums) + 1 == len(nums)
