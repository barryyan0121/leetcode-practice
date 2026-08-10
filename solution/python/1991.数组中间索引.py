"""1991. 数组中间索引"""


class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        left, right = 0, sum(nums)
        for index, value in enumerate(nums):
            right -= value
            if left == right:
                return index
            left += value
        return -1


if __name__ == "__main__":
    assert Solution().findMiddleIndex([2, 3, -1, 8, 4]) == 3
