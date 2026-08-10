"""2740. 找出分区值"""


class Solution:
    def findValueOfPartition(self, nums: list[int]) -> int:
        nums.sort()
        return min(right - left for left, right in zip(nums, nums[1:]))


if __name__ == "__main__":
    assert Solution().findValueOfPartition([1, 3, 6, 10, 15]) == 2
