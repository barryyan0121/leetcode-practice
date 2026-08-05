"""1991. 找到数组的中间位置"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right = sum(nums)
        left = 0
        for index, value in enumerate(nums):
            right -= value
            if left == right:
                return index
            left += value
        return -1


if __name__ == "__main__":
    test_cases = [(([2, 3, -1, 8, 4],), 3), (([1, -1, 4],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().pivotIndex(*args) == expected
