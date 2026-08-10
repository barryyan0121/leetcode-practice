"""3010. 将数组分成最小代价的子数组 I"""


class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        return nums[0] + sum(sorted(nums[1:])[:2])


if __name__ == "__main__":
    assert Solution().minimumCost([1, 2, 3, 12]) == 6
