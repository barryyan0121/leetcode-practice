"""2971. 寻找最长多边形"""


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        total = sum(nums)
        for index in range(len(nums) - 1, 1, -1):
            total -= nums[index]
            if total > nums[index]:
                return total + nums[index]
        return -1


if __name__ == "__main__":
    assert Solution().largestPerimeter([5, 5, 5]) == 15
