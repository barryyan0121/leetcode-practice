"""2229. 检查数组是否连贯"""


class Solution:
    def isConsecutive(self, nums: list[int]) -> bool:
        return len(set(nums)) == len(nums) and max(nums) - min(nums) + 1 == len(nums)


if __name__ == "__main__":
    assert Solution().isConsecutive([3, 5, 4, 2, 6])
    assert not Solution().isConsecutive([1, 3, 4])
