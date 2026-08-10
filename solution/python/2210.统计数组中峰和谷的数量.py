"""2210. 统计数组中峰和谷的数量"""


class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        values = [
            value for i, value in enumerate(nums) if i == 0 or value != nums[i - 1]
        ]
        return sum(
            (values[i] > values[i - 1]) == (values[i] > values[i + 1])
            for i in range(1, len(values) - 1)
        )
