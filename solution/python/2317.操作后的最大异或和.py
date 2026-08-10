"""2317. 操作后的最大异或和"""


class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        result = 0
        for value in nums:
            result |= value
        return result
