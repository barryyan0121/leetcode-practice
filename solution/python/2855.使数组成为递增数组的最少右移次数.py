"""2855. 使数组成为递增数组的最少右移次数"""


class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        drops = [
            index
            for index in range(len(nums))
            if nums[index] > nums[(index + 1) % len(nums)]
        ]
        if len(drops) > 1:
            return -1
        return 0 if not drops else len(nums) - drops[0] - 1


if __name__ == "__main__":
    assert Solution().minimumRightShifts([3, 4, 5, 1, 2]) == 2
    assert Solution().minimumRightShifts([1, 3, 5]) == 0
    assert Solution().minimumRightShifts([2, 1, 4]) == -1
