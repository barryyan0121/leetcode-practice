"""2164. 对偶数下标和奇数下标分别排序"""


class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        nums[::2] = sorted(nums[::2])
        nums[1::2] = sorted(nums[1::2], reverse=True)
        return nums


if __name__ == "__main__":
    test_cases = [(([4, 1, 2, 3],), [2, 3, 4, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().sortEvenOdd(*args) == expected
