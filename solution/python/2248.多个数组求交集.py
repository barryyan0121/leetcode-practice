"""2248. 多个数组求交集"""


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        common = set(nums[0])
        for values in nums[1:]:
            common &= set(values)
        return sorted(common)
