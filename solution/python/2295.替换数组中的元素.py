"""2295. 替换数组中的元素"""


class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        positions = {value: i for i, value in enumerate(nums)}
        for old, new in operations:
            index = positions.pop(old)
            positions[new] = index
            nums[index] = new
        return nums
