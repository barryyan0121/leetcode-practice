"""3011. 判断一个数组是否可以变为有序"""


class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        sorted_nums = sorted(nums)
        start = 0
        while start < len(nums):
            end = start
            bits = nums[start].bit_count()
            while end < len(nums) and nums[end].bit_count() == bits:
                end += 1
            if sorted(nums[start:end]) != sorted_nums[start:end]:
                return False
            start = end
        return True


if __name__ == "__main__":
    assert Solution().canSortArray([8, 4, 2, 30, 15])
