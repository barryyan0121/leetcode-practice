"""2340. 生成有效数组的最少交换次数"""


class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        min_index = nums.index(min(nums))
        max_index = n - 1 - nums[::-1].index(max(nums))
        return min_index + n - 1 - max_index - (min_index > max_index)
