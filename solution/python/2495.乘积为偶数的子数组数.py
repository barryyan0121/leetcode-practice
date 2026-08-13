"""2495. 乘积为偶数的子数组数"""


class Solution:
    def evenProduct(self, nums: list[int]) -> int:
        total = len(nums) * (len(nums) + 1) // 2
        odd_run = odd_only = 0
        for value in nums:
            if value % 2:
                odd_run += 1
                odd_only += odd_run
            else:
                odd_run = 0
        return total - odd_only


if __name__ == "__main__":
    assert Solution().evenProduct([9, 4]) == 2
