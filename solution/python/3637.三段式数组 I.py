"""3637. 三段式数组 I"""


class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        index = 0
        while index + 1 < len(nums) and nums[index] < nums[index + 1]:
            index += 1
        if index == 0 or index == len(nums) - 1:
            return False
        peak = index
        while index + 1 < len(nums) and nums[index] > nums[index + 1]:
            index += 1
        if index == peak or index == len(nums) - 1:
            return False
        while index + 1 < len(nums) and nums[index] < nums[index + 1]:
            index += 1
        return index == len(nums) - 1


if __name__ == "__main__":
    assert Solution().isTrionic([1, 3, 5, 4, 2, 6])
    assert not Solution().isTrionic([2, 1, 3])
